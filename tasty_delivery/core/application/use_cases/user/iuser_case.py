from abc import abstractmethod

from core.application.use_cases.ibase_use_case import IBaseUseCase


class IUserCase(IBaseUseCase):

    @abstractmethod
    def get_user_by_username(self, user_name: str):
        raise NotImplementedError
