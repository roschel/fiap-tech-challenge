from typing import List

from sqlalchemy import update
from sqlalchemy.exc import IntegrityError

from tasty_delivery.adapter.database.models.user import User as UserDb
from tasty_delivery.core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from tasty_delivery.core.domain.repositories.iuser_repository import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self, db=None):
        self.db = db

    def get_all(self) -> List[UserDb]:
        result = self.db.query(UserDb).all()
        return result

    def get_by_id(self, id) -> UserDb:
        result = self.db.query(UserDb).filter(UserDb.id == id).scalar()
        if not result:
            raise ObjectNotFound(f"Usuário {id} não encontrado", 404)
        return result

    def create(self, obj: UserDb) -> UserDb:
        try:
            self.db.add(obj)
            self.db.flush()
            self.db.refresh(obj)
            self.db.commit()
        except IntegrityError:
            raise DuplicateObject("Usuário já existente na base de dados", 409)
        return obj

    def update(self, id, new_values):
        update(UserDb).where(UserDb.id == id).values(new_values)
