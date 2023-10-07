from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from logger import logger
from tasty_delivery.adapter.database.models.category import Category as CategoryDB
from tasty_delivery.adapter.repositories.category_repository import CategoryRepository
from tasty_delivery.core.application.use_cases.category.icategory_case import ICategoryCase
from tasty_delivery.core.domain.entities.category import Category


class CategoryCase(ICategoryCase):

    def __init__(self, db=None):
        self.repository = CategoryRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        result = self.repository.get_by_id(id)
        if not result:
            msg = f"Categoria {id} não encontrado"
            logger.warning(msg)
            raise ObjectNotFound(msg, 404)
        return result

    def create(self, obj: Category) -> Category:
        obj.id = uuid4()
        try:
            return self.repository.create(CategoryDB(**vars(obj)))
        except IntegrityError:
            msg = "Categoria já existente na base de dados"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)

    def update(self, id, new_values: Category) -> Category:
        new_values.id = None
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    def delete(self, id):
        return self.repository.delete(id)
