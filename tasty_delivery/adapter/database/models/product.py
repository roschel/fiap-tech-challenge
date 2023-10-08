from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column

from adapter.database.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(UUID, primary_key=True, index=True)
    nome = Column(String)
    is_active = Column(BOOLEAN)
    is_deleted = Column(BOOLEAN)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow())
    category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"))
    created_by: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    updated_by: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=True)
