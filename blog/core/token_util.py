import logging

import jwt
from datetime import timedelta, datetime

from fastapi import HTTPException
from jwt.algorithms import HMACAlgorithm
import time

from blog.core.config import SECRET_KEY
from blog.models.domain.users import CurrentUser
from blog.models.mapper.users_mapper import LoginAccount


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")


def decode_token(token: str) -> CurrentUser:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        print(type(payload))
        username: str = payload.get("user_name")
        if not username:
            raise HTTPException(status_code=401, detail="解析token失败，用户信息异常")
        else:
            # 校验用户信息？
            # 创建user对象 放入 threadLocal
            print(username)
            return CurrentUser(user_name=username)
    except Exception as e:
        logging.error(e)
    # raise HTTPException(status_code=401, detail="解析token使用，用户信息异常")

# if __name__ == '__main__':
#     expire = datetime.now() + timedelta(minutes=15)
#     print(str(expire))
