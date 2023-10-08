from pydantic import Field

from core.domain.entities.base_entity import Base


class Category(Base):
    nome: str = Field(title="Descrição da categoria")
