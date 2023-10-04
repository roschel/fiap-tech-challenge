from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from tasty_delivery.adapter.database.db import get_db
from tasty_delivery.core.application.use_cases.product.product_case import ProductCase
from tasty_delivery.core.domain.entities.product import Product as Product
from tasty_delivery.core.domain.exceptions.exception_schema import ObjectNotFound, ObjectDuplicated


class ProductController:

    def __init__(self, product_case: ProductCase = None):
        self.router = APIRouter(tags=["Products"], prefix='/products')
        self.router.add_api_route(
            path="/",
            endpoint=self.products,
            methods=["GET"],
            response_model=List[Product],
            status_code=200
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.product_by_id,
            methods=["GET"],
            response_model=Product,
            responses={
                200: {"model": Product},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200
        )
        self.router.add_api_route(
            path="/categories/{category_id}",
            endpoint=self.products_by_category,
            methods=["GET"],
            response_model=List[Product],
            status_code=200
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create,
            methods=["POST"],
            response_model=Product,
            responses={
                201: {"model": Product},
                409: {"model": ObjectDuplicated}
            },
            status_code=201
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.update,
            methods=["PUT"],
            response_model=Product,
            responses={
                200: {"model": Product},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.delete,
            methods=["DELETE"],
            response_model=Product,
            responses={
                200: {"model": Product},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200
        )

        self._product_case = product_case

    async def products(self, db=Depends(get_db)):
        return self._product_case(db).get_all()

    async def product_by_id(self, id: int, db=Depends(get_db)):
        return self._product_case(db).get_by_id(id)

    async def products_by_category(self, category_id: int, db=Depends(get_db)):
        return self._product_case(db).get_by_category(category_id)

    async def create(self, product: Product, db=Depends(get_db)):
        return self._product_case(db).create(product)

    async def update(self, id: int, product: Product, db=Depends(get_db)):
        return self._product_case(db).update(id, product)

    async def delete(self, id: UUID, db=Depends(get_db)):
        return self._product_case(db).delete(id)
