from typing import List

from sqlalchemy.exc import IntegrityError

from tasty_delivery.core.domain.entities.user import User
from tasty_delivery.adapter.database.models.user import User as UserDB
from tasty_delivery.core.application.use_cases.iuser_case import IUserCase
from tasty_delivery.core.domain.exceptions.user_exception import DuplicateUser


class UserCase(IUserCase):

    def get_users(self) -> List[User]:
        return self.repository.get_users()

    def create(self, user: User) -> User:
        try:
            return self.repository.create(UserDB(**vars(user)))
        except IntegrityError:
            raise DuplicateUser("Usuário já existente na base de dados", 409)

