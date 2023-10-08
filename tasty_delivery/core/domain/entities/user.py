from pydantic import Field

from core.domain.entities.base_entity import Base


class User(Base):
    nome: str = Field()
    email: str = Field()
    cpf: str = Field(max_length=11)
    username: str = Field()
    password: str = Field(serialization_alias='hashed_password')


class UserOUT(User):
    password: str = Field(None, exclude=True)


class UserInDB(User):
    hashed_password: str = Field()


class UserUpdate(Base):
    nome: str = Field(None)
    email: str = Field(None)
    cpf: str = Field(None, max_length=11)
