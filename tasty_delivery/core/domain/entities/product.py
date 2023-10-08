from uuid import UUID

from pydantic import Field

from core.domain.entities.base_entity import Base
from core.domain.entities.category import Category


class ProductIN(Base):
    nome: str = Field()
    descricao: str = Field()
    preco: float = Field(gt=0)
    category_id: UUID = Field()


class ProductUpdate(Base):
    nome: str | None = Field(None)
    descricao: str | None = Field(None)
    preco: float | None = Field(gt=0)
    category_id: UUID | None = Field(None)


class ProductOUT(Base):
    nome: str = Field()
    descricao: str = Field()
    preco: float = Field(gt=0)
    category: Category | None = Field(None)
