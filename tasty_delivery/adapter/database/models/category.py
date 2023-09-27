from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped

from tasty_delivery.adapter.database.db import Base
from tasty_delivery.adapter.database.models.product import Product


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    products: Mapped[List[Product]] = relationship()

