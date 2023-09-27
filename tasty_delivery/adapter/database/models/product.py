from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from tasty_delivery.adapter.database.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
