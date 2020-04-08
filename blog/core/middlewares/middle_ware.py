from time import time

from fastapi import Request


async def token_middle(request: Request, call_next):
    start = time()
    print(start)
    print(str(request))
    print(request.scope.get("path"))

    # 下面 业务代码执行完毕后 才会执行
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(start)
    return response
