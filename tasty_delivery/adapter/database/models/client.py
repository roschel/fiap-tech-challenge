from datetime import datetime

from sqlalchemy import Column, String, BOOLEAN, TIMESTAMP, UUID, ARRAY

from adapter.database.db import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(UUID, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    cpf = Column(String, unique=True)
    is_active = Column(BOOLEAN)
    is_deleted = Column(BOOLEAN)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow())
    scopes = Column(ARRAY(String), nullable=True)
