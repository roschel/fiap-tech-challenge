from abc import abstractmethod
from tasty_delivery.core.application.use_cases.ibase_use_case import IBaseUseCase


class IUserCase(IBaseUseCase):

    @abstractmethod
    def authenticate_user(self, form_data):
        raise NotImplementedError
