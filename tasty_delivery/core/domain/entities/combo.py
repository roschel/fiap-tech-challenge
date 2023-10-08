from pydantic import Field

from core.domain.entities.base_entity import Base
from core.domain.entities.client import Client


class Combo(Base):
    cliente: Client
    nome: str = Field(title="Descrição do combo")
    preco: float = Field(title="Preço do combo")
    lanche: str = Field(title="Lanche do combo")
    acompanhamento: str = Field(title="Acompanhamento do combo")
    bebida: str = Field(title="Bebida do combo")
    quantidade: int = Field(title="Quantidade do combo")
    desconto: float = Field(title="Desconto do combo")
    total: float = Field(title="Total do combo")
