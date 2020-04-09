from typing import Optional


class Result(object):
    def __init__(self, data=None, code: int = 200, msg: str = "success"):
        self.code = code
        self.msg = msg
        # if data:
        self.data = data
