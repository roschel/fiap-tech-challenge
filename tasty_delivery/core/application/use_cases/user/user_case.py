from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from logger import logger
from tasty_delivery.adapter.database.models.user import User as UserDB
from tasty_delivery.adapter.repositories.user_repository import UserRepository
from tasty_delivery.core.application.use_cases.user.iuser_case import IUserCase
from tasty_delivery.core.domain.entities.user import User


class UserCase(IUserCase):

    def __init__(self, db=None):
        self.repository = UserRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        result = self.repository.get_by_id(id)
        if not result:
            msg = f"Usuário {id} não encontrado"
            logger.warning(msg)
            raise ObjectNotFound(msg, 404)
        return result

    def create(self, obj: User) -> User:
        try:
            obj.id = uuid4()
            return self.repository.create(UserDB(**vars(obj)))
        except IntegrityError:
            msg = "Usuário já existente na base de dados"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)

    def update(self, id, new_values: User) -> User:
        new_values.id = None
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    def delete(self, id):
        return self.repository.delete(id)

    def get_user_by_username(self, user_name: str):
        return self.repository.get_user_by_username(user_name)
