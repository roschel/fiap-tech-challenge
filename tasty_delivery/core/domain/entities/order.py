from typing import Annotated, List
from uuid import UUID

from pydantic import Field

from core.domain.entities.base_entity import Base

class OrderIN(Base):
    produtos: Annotated[List, UUID] = Field()
    preco: float = Field(gt=0)
    quantidade: int = Field(gt=0)
    desconto: float = Field(ge=0)
    total: float = Field(gt=0)
    status: str = Field()

class OrderUpdate(Base):
    produtos: Annotated[List, UUID] | None = Field()
    preco: float | None = Field(gt=0)
    quantidade: int| None = Field(gt=0)
    desconto: float | None = Field(ge=0)
    total: float | None = Field(gt=0)
    status: str | None = Field(None)


class OrderOUT(Base):
    produtos: Annotated[List, UUID] = Field()
    preco: float = Field(gt=0)
    quantidade: int = Field(gt=0)
    desconto: float = Field(ge=0)
    total: float = Field(gt=0)
    status: str = Field()
