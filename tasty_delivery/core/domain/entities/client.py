from pydantic import Field

from core.domain.entities.base_entity import Base


class Client(Base):
    nome: str = Field()
    email: str = Field()
    cpf: str = Field(max_length=11)
