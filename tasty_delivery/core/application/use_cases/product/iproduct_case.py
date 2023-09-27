from abc import abstractmethod
from tasty_delivery.core.application.use_cases.ibase_use_case import IBaseUseCase


class IProductCase(IBaseUseCase):

    @abstractmethod
    def get_by_category(self, category_id):
        raise NotImplementedError
