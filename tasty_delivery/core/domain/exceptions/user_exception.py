from fastapi import HTTPException


class DuplicateUser(HTTPException):
    def __init__(self, msg: str, status_code: int):
        super(DuplicateUser, self).__init__(status_code=status_code, detail=msg)


class UserNotFound(HTTPException):
    def __init__(self, msg: str, status_code: int):
        super(UserNotFound, self).__init__(status_code=status_code, detail=msg)
