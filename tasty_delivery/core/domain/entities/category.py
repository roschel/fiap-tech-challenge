from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int = Field(None)
    nome: str = Field(title="Descrição da categoria")
