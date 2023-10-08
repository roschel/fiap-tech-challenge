from uuid import UUID

from pydantic import Field

from core.domain.entities.base_entity import Base
from core.domain.entities.category import Category


class ProductIN(Base):
    nome: str = Field()
    descricao: str = Field()
    preco: float = Field(gt=0)
    category_id: UUID = Field()


class ProductOUT(Base):
    nome: str = Field()
    descricao: str = Field()
    preco: float = Field(gt=0)
    category: Category | None = Field(None)
