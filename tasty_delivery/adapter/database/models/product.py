from datetime import datetime
from typing import List

from sqlalchemy import Column, String, ForeignKey, BOOLEAN, TIMESTAMP, UUID, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from adapter.database.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(UUID, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    is_active = Column(BOOLEAN)
    is_deleted = Column(BOOLEAN)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow())
    #category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"))
    #category: Mapped["Category"] = relationship(viewonly=True)
    category_id = Column(UUID, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products", viewonly=True)
    created_by: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    updated_by: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=True)
    order_id = Column(UUID, ForeignKey('orders.id'))
    order = relationship("Order", back_populates="products", viewonly=True)
    
