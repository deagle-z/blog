class BusinessException(Exception):
    def __init__(self, code=500, msg="业务错误"):
        self.code = code
        self.msg = msg
