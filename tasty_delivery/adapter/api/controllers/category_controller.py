from typing import List

from fastapi import APIRouter, Depends

from tasty_delivery.adapter.database.db import get_db
from tasty_delivery.core.application.use_cases.category.category_case import CategoryCase
from tasty_delivery.core.domain.entities.category import Category as Category
from tasty_delivery.core.domain.exceptions.exception_schema import ObjectNotFound, ObjectDuplicated


class CategoryController:

    def __init__(self, category_case: CategoryCase = None):
        self.router = APIRouter(tags=["Categories"], prefix='/categories')
        self.router.add_api_route(
            path="/",
            endpoint=self.categories,
            methods=["GET"],
            response_model=List[Category],
            status_code=200
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.category_by_id,
            methods=["GET"],
            response_model=Category,
            responses={
                200: {"model": Category},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create,
            methods=["POST"],
            response_model=Category,
            responses={
                201: {"model": Category},
                409: {"model": ObjectDuplicated}
            },
            status_code=201
        )

        self._category_case = category_case

    async def categories(self, db=Depends(get_db)):
        return self._category_case(db).get_all()

    async def category_by_id(self, id: int, db=Depends(get_db)):
        return self._category_case(db).get_by_id(id)

    async def create(self, category: Category, db=Depends(get_db)):
        return self._category_case(db).create(category)
