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
        return self.repository.get_by_id(id)

    def create(self, obj: Category) -> Category:
        return self.repository.create(CategoryDB(**vars(obj)))

    def update(self, id, new_values: Category) -> Category:
        return self.repository.update(id, new_values.model_dump(exclude_none=True))
