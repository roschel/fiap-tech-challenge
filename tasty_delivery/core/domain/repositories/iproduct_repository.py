from abc import abstractmethod

from tasty_delivery.core.domain.repositories.ibase_repository import IBaseRepository


class IProductRepository(IBaseRepository):

    @abstractmethod
    def get_by_category(self, category_id):
        raise NotImplementedError
