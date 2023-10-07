from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from logger import logger
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
        result = self.repository.get_by_id(id)
        if not result:
            msg = f"Produto {id} não encontrado"
            logger.warning(msg)
            raise ObjectNotFound(msg, 404)
        return result

    def get_by_category(self, category_id):
        return self.repository.get_by_category(category_id)

    def create(self, obj: Product) -> Product:
        try:
            obj.id = uuid4()
            return self.repository.create(ProductDB(**vars(obj)))
        except IntegrityError:
            msg = "Produto já existente na base de dados"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)

    def update(self, id, new_values: Product) -> Product:
        new_values.id = None
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    def delete(self, id):
        return self.repository.delete(id)
