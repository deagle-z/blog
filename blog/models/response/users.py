from typing import Optional

from pydantic import BaseModel, BaseConfig

from blog.models.response.baseconfig import RWSchema


class User4Response(RWSchema):
    id: Optional[int]
    user_name: Optional[str]
    nick_name: Optional[str]
    e_mail: Optional[str]


