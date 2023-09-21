from abc import ABC
from typing import List

from tasty_delivery.core.application.use_cases.base_use_case import BaseUseCase
from tasty_delivery.core.domain.entities.user import User


class IUserCase(ABC, BaseUseCase):

    def get_users(self) -> List[User]:
        raise NotImplementedError

    def create(self, user: User) -> User:
        raise NotImplementedError
