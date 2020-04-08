from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

SQLALCHEMY_DATABASE_URL = "mysql://root:123456@localhost:3306/blog"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    , echo=True  # console输b入sql
    , echo_pool=True  # 连接池将记录信息输出
    # ,encoding="utf-8"
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


# logger.log("connection to ${0}", SQLALCHEMY_DATABASE_URL)


# Dependency , 获取会话
def connection_to_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()
