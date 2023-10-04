from datetime import datetime
from typing import List

from sqlalchemy import Column, String, BOOLEAN, TIMESTAMP, UUID
from sqlalchemy.orm import relationship, Mapped

from tasty_delivery.adapter.database.db import Base
from tasty_delivery.adapter.database.models.product import Product


class Category(Base):
    __tablename__ = 'categories'

    id = Column(UUID, primary_key=True, index=True)
    nome = Column(String)
    is_active = Column(BOOLEAN)
    is_deleted = Column(BOOLEAN)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow())
    products: Mapped[List[Product]] = relationship()

