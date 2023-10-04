from pydantic import Field

from tasty_delivery.core.domain.entities.base_entity import Base


class User(Base):
    nome: str = Field()
    email: str = Field()
    cpf: str = Field(max_length=11)


class UserUpdate(Base):
    nome: str = Field(None)
    email: str = Field(None)
    cpf: str = Field(None, max_length=11)
