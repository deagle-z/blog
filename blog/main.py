from time import time

from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.security import OAuth2PasswordBearer
import uvicorn
import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from blog.api.api import router
from fastapi import Request

from blog.core.exception.exceptions import BusinessException
from blog.core.middlewares.middle_ware import token_middle
from blog.core.response import Result


def get_application() -> FastAPI:
    application = FastAPI(title="blog", debug=True, version="0.0.1")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        # allow_credentials = True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    application.include_router(router)
    # application.add_exception_handler()
    return application


app = get_application()


@app.exception_handler(HTTPException)
async def business_exception_handler(request, exc):
    if type(exc) is HTTPException:
        return Result(code=exc.code, msg=exc.msg)
    # else:
    #     return Result(code=500, msg="未知异常")


@app.middleware("http")
async def token_middle_ware(request: Request, call_next):
    return await token_middle(request=request, call_next=call_next)


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000, debug=True)
