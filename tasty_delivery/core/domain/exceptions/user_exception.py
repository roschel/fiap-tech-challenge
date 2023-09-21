from fastapi import HTTPException
from pydantic import BaseModel, Field

USER_DUPLICATED_MESSAGE = "Usuário duplicado na base de dados"


class DefaultResponse(BaseModel):
    def __init__(self):
        super(DefaultResponse, self).__init__()

    detail: str = Field(
        default="Problema de conexão com o banco de dados",
        title="Mensagem",
        description="Mensagem de erro ou descrição do retorno",
        example="Internal Server Error!"
    )


class UserNotFound(DefaultResponse):
    detail: str = Field(
        default=USER_DUPLICATED_MESSAGE,
        title="Mensagem",
        description=USER_DUPLICATED_MESSAGE,
        example=USER_DUPLICATED_MESSAGE
    )


class DuplicateUser(HTTPException):
    def __init__(self, msg: str, status_code: int):
        super(DuplicateUser, self).__init__(status_code=status_code, detail=msg)
