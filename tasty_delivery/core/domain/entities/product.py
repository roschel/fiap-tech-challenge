from pydantic import Field

from core.domain.entities.base_entity import Base


class Product(Base):
    nome: str = Field()
    category_id: str = Field()
