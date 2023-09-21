from sqlalchemy import Column, Integer, Float, DateTime, String

from tasty_delivery.adapter.database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    cpf = Column(String)
