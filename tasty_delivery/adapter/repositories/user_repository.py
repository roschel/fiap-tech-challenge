from typing import List

from sqlalchemy.exc import IntegrityError

from tasty_delivery.adapter.database.models.user import User as UserDb
from tasty_delivery.core.domain.exceptions.user_exception import DuplicateUser, UserNotFound
from tasty_delivery.core.domain.repositories.iuser_repository import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self, db=None):
        self.db = db

    def get_users(self) -> List[UserDb]:
        result = self.db.query(UserDb).all()
        return result

    def get_user_by_id(self, id) -> UserDb:
        result = self.db.query(UserDb).filter(UserDb.id == id).scalar()
        if not result:
            raise UserNotFound(f"Usuário {id} não encontrado", 404)
        return result

    def create(self, user: UserDb) -> UserDb:
        try:
            self.db.add(user)
            self.db.flush()
            self.db.refresh(user)
            self.db.commit()
        except IntegrityError:
            raise DuplicateUser("Usuário já existente na base de dados", 409)
        return user
