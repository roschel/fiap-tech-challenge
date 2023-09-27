from abc import abstractmethod, ABC
from typing import List

from tasty_delivery.core.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_id(self, id) -> User:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError
