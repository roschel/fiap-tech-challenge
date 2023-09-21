from typing import List

from tasty_delivery.adapter.api.models.user import User as UserSchema
from tasty_delivery.adapter.database.models.user import User as UserDB
from tasty_delivery.core.application.use_cases.iuser_case import IUserCase


class UserCase(IUserCase):

    def get_users(self) -> List[UserSchema]:
        return self.repository.get_users()

    def create(self, user: UserSchema) -> UserSchema:
        result = self.repository.create(UserDB(**vars(user)))
        return result

