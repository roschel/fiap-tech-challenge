from typing import Annotated, List

from pydantic import Field, BaseModel

from core.domain.entities.base_entity import Base


class Client(Base):
    nome: str = Field()
    email: str = Field()
    cpf: str = Field(max_length=11)
    scopes: Annotated[List, str] = Field([])


class ClientUpdate(BaseModel):
    nome: str = Field()
    email: str = Field()
    cpf: str = Field(max_length=11)
