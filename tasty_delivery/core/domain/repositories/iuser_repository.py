from abc import abstractmethod
from core.domain.repositories.ibase_repository import IBaseRepository


class IUserRepository(IBaseRepository):

    @abstractmethod
    def get_user_by_username(self, user_name: str):
        raise NotImplementedError
