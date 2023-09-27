from typing import List

from sqlalchemy.exc import IntegrityError

from tasty_delivery.adapter.database.models.category import Category as CategoryDb
from tasty_delivery.core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from tasty_delivery.core.domain.repositories.icategory_repository import ICategoryRepository


class CategoryRepository(ICategoryRepository):

    def __init__(self, db=None):
        self.db = db

    def get_all(self) -> List[CategoryDb]:
        result = self.db.query(CategoryDb).all()
        return result

    def get_by_id(self, id) -> CategoryDb:
        result = self.db.query(CategoryDb).filter(CategoryDb.id == id).scalar()
        if not result:
            raise ObjectNotFound(f"Categoria {id} não encontrado", 404)
        return result

    def create(self, obj: CategoryDb) -> CategoryDb:
        try:
            self.db.add(obj)
            self.db.flush()
            self.db.refresh(obj)
            self.db.commit()
        except IntegrityError:
            raise DuplicateObject("Categoria já existente na base de dados", 409)
        return obj
