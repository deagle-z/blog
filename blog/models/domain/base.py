import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, DATETIME

from pydantic import BaseConfig, BaseModel
from blog.db.base import base


def convert_datetime_to_realworld(dt: datetime.datetime) -> str:
    return dt.replace(tzinfo=datetime.timezone.dst(dt="sh")).isoformat().replace("+00:00", "Z")


def convert_field_to_camel_case(string: str) -> str:
    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )


class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {datetime.datetime: convert_datetime_to_realworld}
        alias_generator = convert_field_to_camel_case


class BlogModel():
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    create_time = Column(DATETIME)
    create_by = Column(String)
    update_time = Column(DATETIME)
    update_by = Column(String)
    is_delete = Column(String)
