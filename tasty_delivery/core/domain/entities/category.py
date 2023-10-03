from pydantic import Field

from tasty_delivery.core.domain.entities.base_entity import Base


class Category(Base):
    nome: str = Field(title="Descrição da categoria")
