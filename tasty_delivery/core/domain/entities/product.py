from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int = Field(None)
    nome: str = Field()
    category_id: int = Field()
