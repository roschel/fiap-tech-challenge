from uuid import uuid4

from tasty_delivery.adapter.database.models.product import Product as ProductDB
from tasty_delivery.adapter.repositories.product_repository import ProductRepository
from tasty_delivery.core.application.use_cases.product.iproduct_case import IProductCase
from tasty_delivery.core.domain.entities.product import Product


class ProductCase(IProductCase):
    def __init__(self, db=None):
        self.repository = ProductRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def get_by_category(self, category_id):
        return self.repository.get_by_category(category_id)

    def create(self, obj: Product) -> Product:
        obj.id = uuid4()
        return self.repository.create(ProductDB(**vars(obj)))

    def update(self, id, new_values: Product) -> Product:
        return self.repository.update(id, new_values.model_dump(exclude_none=True))
