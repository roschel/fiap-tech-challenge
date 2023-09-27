from pydantic import BaseModel, Field

USER_NOT_FOUND_MESSAGE = "Usuário não encontrado"
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
        default=USER_NOT_FOUND_MESSAGE,
        title="Mensagem",
        description=USER_NOT_FOUND_MESSAGE,
        example=USER_NOT_FOUND_MESSAGE
    )


class UserDuplicated(DefaultResponse):
    detail: str = Field(
        default=USER_DUPLICATED_MESSAGE,
        title="Mensagem",
        description=USER_DUPLICATED_MESSAGE,
        example=USER_DUPLICATED_MESSAGE
    )