from typing import List

from tasty_delivery.adapter.database.db import get_db
from tasty_delivery.core.domain.repositories.iuser_repository import IUserRepository
from tasty_delivery.adapter.database.models.user import User as UserDb


class UserRepository(IUserRepository):

    def __init__(self):
        self.db = get_db()

    def get_users(self) -> List[UserDb]:
        result = self.db.query(UserDb).all()
        return result

    def create(self, user: UserDb) -> UserDb:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        self.db.commit()
        return user
