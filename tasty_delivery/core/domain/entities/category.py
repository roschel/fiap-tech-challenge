from pydantic import Field, BaseModel

from core.domain.entities.base_entity import Base


class CategoryIN(BaseModel):
    nome: str = Field(title="Descrição da categoria")


class CategoryOUT(Base):
    nome: str = Field(title="Descrição da categoria")
