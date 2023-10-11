from datetime import datetime
from typing import List

from sqlalchemy import Column, String, Float, Boolean, TIMESTAMP, Integer, UUID, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from adapter.database.db import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(UUID, primary_key=True, index=True)
    client_id = Column(String)
    is_active = Column(Boolean)
    is_deleted = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow)
    created_by: Mapped[UUID] = mapped_column(ForeignKey("clients.id"))
    updated_by: Mapped[UUID] = mapped_column(ForeignKey("clients.id"), nullable=True)
    total = Column(Float)
    quantidade = Column(Integer)
    desconto = Column(Float)
    status = Column(String)
    # Relação com Produtos
    product_id = Column(UUID, ForeignKey("products.id"))
