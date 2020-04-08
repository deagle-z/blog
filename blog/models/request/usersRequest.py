from typing import Union

from pydantic import BaseModel


class SimpleUser(BaseModel):
    user_name: str
    password: str
