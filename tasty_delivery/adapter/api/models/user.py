from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(None)
    nome: str = Field()
    email: str = Field()
    cpf: str = Field(max_length=11)
