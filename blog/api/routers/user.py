import uvicorn
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from blog.core import token_util
from blog.core.response import Result
from blog.db.base import connection_to_db
from blog.db.users import UserRepository
from blog.models.request.usersRequest import SimpleUser
from blog.models.response.users import User4Response

router = APIRouter()


@router.get("/getUserId/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(connection_to_db)):
    user = UserRepository(db).get_user_by_id(user_id)
    if user:
        print(user.e_mail)
    else:
        print("user is none")
    return Result(data=user)


@router.post("/login")
async def login(user: SimpleUser, db: Session = Depends(connection_to_db)):
    # todo 校验验证码
    user = UserRepository(db).get_user_by_name(user.user_name)
    if user and user.password:
        if user.password == user.password:
            return Result(data={
                "token": token_util.create_access_token(data={"user_name": user.user_name, "password": user.password})})
        return Result.error("密码错误")
    return Result.error("不存在的用户")
