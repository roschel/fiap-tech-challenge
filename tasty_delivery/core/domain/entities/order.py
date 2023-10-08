from pydantic import Field

from core.domain.entities.base_entity import Base
from core.domain.entities.client import Client


class Order(Base):
    cliente: Client
    nome: str = Field(title="Descrição do pedido")
    preco: float = Field(title="Preço do pedido")
    lanche: str = Field(title="Lanche do pedido")
    acompanhamento: str = Field(title="Acompanhamento do pedido")
    bebida: str = Field(title="Bebida do pedido")
    quantidade: int = Field(title="Quantidade do pedido")
    desconto: float = Field(title="Desconto do pedido")
    total: float = Field(title="Total do pedido")

