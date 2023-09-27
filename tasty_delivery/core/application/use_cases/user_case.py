from typing import List

from tasty_delivery.adapter.database.models.user import User as UserDB
from tasty_delivery.adapter.repositories.user_repository import UserRepository
from tasty_delivery.core.application.use_cases.iuser_case import IUserCase
from tasty_delivery.core.domain.entities.user import User


class UserCase(IUserCase):
    def __init__(self, db=None):
        self.repository = UserRepository(db)

    def get_users(self) -> List[User]:
        return self.repository.get_users()

    def get_user_by_id(self, id):
        return self.repository.get_user_by_id(id)

    def create(self, user: User) -> User:
        return self.repository.create(UserDB(**vars(user)))
