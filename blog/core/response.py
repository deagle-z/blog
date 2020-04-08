from typing import Optional


class Result(object):
    def __init__(self, data=Optional[None], code: int = 200, msg: str = "success"):
        self.code = code
        self.msg = msg
        self.data = data

    @staticmethod
    def error(self, code: int = 500, msg: str = "error"):
        self.code = code
        self.msg = msg
        return self
