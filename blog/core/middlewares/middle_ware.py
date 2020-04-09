import re
from time import time
from fastapi import Request
from fastapi.exceptions import HTTPException
from blog.core.config import EXCLUDE_URL
from blog.core.exception.exceptions import BusinessException
from blog.core.token_util import decode_token
import threading

local = threading.local()


async def token_middle(request: Request, call_next):
    start: float = time() * 1000
    path = request.url.path
    for index, url in enumerate(EXCLUDE_URL):
        if re.match(url, path):
            break
        else:
            # 对token 进行校验等判断
            token = request.headers.get("Authorization")
            if token:
                login_account = decode_token(token)
                local.login_account = login_account
            else:
                raise BusinessException(msg="用户信息异常")
                # raise HTTPException(status_code=500, detail="用户信息异常")

    # 下面 业务代码执行完毕后 才会执行
    response = await call_next(request)
    end = time() * 1000
    response.headers["X-Process-Time"] = str(end - start)
    print("-----%s----接口执行时间:%d毫秒" % (path, end - start))
    print(local.login_account)
    return response
