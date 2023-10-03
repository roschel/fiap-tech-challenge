from pydantic import Field

from tasty_delivery.core.domain.entities.base_entity import Base


class Product(Base):
    nome: str = Field()
    category_id: int = Field()
