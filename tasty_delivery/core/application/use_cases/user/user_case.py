from uuid import uuid4

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
        return self.repository.get_by_id(id)

    def create(self, obj: User) -> User:
        obj.id = uuid4()
        return self.repository.create(UserDB(**vars(obj)))

    def update(self, id, new_values: User) -> User:
        return self.repository.update(id, new_values.model_dump(exclude_none=True))
