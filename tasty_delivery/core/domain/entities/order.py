from pydantic import Field

from core.domain.entities.base_entity import Base
from core.domain.entities.client import Client


class OrderIN(Base):
    client: Client = Field()
    preco: float = Field(gt=0)
    lanche: str | None = Field(None)
    acompanhamento: str | None = Field(None)
    bebida: str | None = Field(None)
    quantidade: int = Field(gt=0)
    desconto: float = Field(gt=0)
    total: float = Field(gt=0)
    status: str = Field()

class OrderUpdate(Base):
    client: Client | None = Field(None)
    preco: float | None = Field(gt=0)
    lanche: str | None = Field(None)
    acompanhamento: str | None = Field(None)
    bebida: str | None = Field(None)
    quantidade: int| None = Field(gt=0)
    desconto: float | None = Field(gt=0)
    total: float | None = Field(gt=0)
    status: str | None = Field(None)


class OrderOUT(Base):
    client: Client = Field()
    preco: float = Field(gt=0)
    lanche: str | None = Field(None)
    acompanhamento: str | None = Field(None)
    bebida: str | None = Field(None)
    quantidade: int = Field(gt=0)
    desconto: float = Field(gt=0)
    total: float = Field(gt=0)
    status: str = Field()
