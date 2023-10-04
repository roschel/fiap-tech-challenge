from datetime import datetime

from sqlalchemy import Column, Integer, String, BOOLEAN, TIMESTAMP, UUID

from tasty_delivery.adapter.database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    cpf = Column(String, unique=True)
    is_active = Column(BOOLEAN)
    is_deleted = Column(BOOLEAN)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow())
