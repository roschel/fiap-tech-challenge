from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import Field, BaseModel

from core.domain.entities.client import Client
from core.domain.entities.product import ProductOUT


class OrderBase(BaseModel):
    id: int = Field(None)
    is_active: bool = Field(True)
    is_deleted: bool = Field(False)
    created_at: datetime | None = Field(None)
    updated_at: datetime | None = Field(None)
    created_by: UUID | None = Field(None)
    updated_by: UUID | None = Field(None)


class Produto(BaseModel):
    produto: ProductOUT = Field()
    quantidade: int | None = Field()
    obs: str | None = Field(None)


class OrderIN(BaseModel):
    produtos: List[Produto] = Field()
    desconto: float = Field(gte=0)
    total: float = Field(gte=0)


class OrderUpdate(OrderBase):
    client: Client | None = Field(None)
    produtos: List[Produto] = Field()
    desconto: float | None = Field(gte=0)
    total: float | None = Field(gte=0)
    status: str | None = Field(None)


class OrderOUT(OrderBase):
    client: Client | None = Field(None)
    produtos: List[Produto] = Field()
    desconto: float | None = Field(gte=0)
    total: float | None = Field(gte=0)
    status: str | None = Field()
