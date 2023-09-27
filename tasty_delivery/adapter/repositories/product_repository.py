from typing import List

from sqlalchemy import update
from sqlalchemy.exc import IntegrityError

from tasty_delivery.adapter.database.models.product import Product as ProductDb
from tasty_delivery.core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from tasty_delivery.core.domain.repositories.iproduct_repository import IProductRepository


class ProductRepository(IProductRepository):

    def __init__(self, db=None):
        self.db = db

    def get_all(self) -> List[ProductDb]:
        result = self.db.query(ProductDb).all()
        return result

    def get_by_id(self, id) -> ProductDb:
        result = self.db.query(ProductDb).filter(ProductDb.id == id).scalar()
        if not result:
            raise ObjectNotFound(f"Produto {id} não encontrado", 404)
        return result

    def get_by_category(self, category_id) -> List[ProductDb]:
        return self.db.query(ProductDb).filter(ProductDb.category_id == category_id).all()

    def create(self, obj: ProductDb) -> ProductDb:
        try:
            self.db.add(obj)
            self.db.flush()
            self.db.refresh(obj)
            self.db.commit()
        except IntegrityError:
            raise DuplicateObject("Produto já existente na base de dados", 409)
        return obj

    def update(self, id, new_values):
        self.db.query(ProductDb).filter(ProductDb.id == id).update(new_values)
        self.db.flush()
        self.db.commit()
        return self.get_by_id(id)
