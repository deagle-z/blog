from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, DATETIME, Table, MetaData
from .base import BlogModel, RWModel
from ...db.base import base


class User(BlogModel, base):
    __tablename__ = "user"
    user_name = Column(String)
    password = Column(String)
    nick_name = Column(String)
    e_mail = Column(String, unique=True)


class CurrentUser:
    def __init__(self, user_name=str, ):
        self.user_name = user_name
