from uuid import UUID

from pydantic import Field, BaseModel

from core.domain.entities.base_entity import Base
from core.domain.entities.category import CategoryOUT


class ProductIN(BaseModel):
    nome: str = Field()
    descricao: str = Field()
    preco: float = Field(gt=0)
    category_id: UUID = Field()


class ProductUpdateIN(BaseModel):
    nome: str | None = Field(None)
    descricao: str | None = Field(None)
    preco: float | None = Field(gt=0)
    category_id: UUID | None = Field(None)


class ProductOUT(Base):
    nome: str = Field()
    descricao: str = Field()
    preco: float = Field(gt=0)
    category: CategoryOUT | None = Field(None)
