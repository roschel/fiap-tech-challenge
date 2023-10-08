from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from adapter.database.db import get_db
from core.application.use_cases.order.order_case import OrderCase
from core.domain.entities.order import Order, Combo
from core.domain.exceptions.exception_schema import ObjectNotFound, ObjectDuplicated
from security import get_current_user


class OrderController:
    
    def __init__(self, order_case: OrderCase = None):
        self.router = APIRouter(
            tags=["Orders"], 
            prefix="/orders"
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.orders,
            methods=["GET"],
            response_model=List[Order],
            status_code=200,
            response_model_exclude_none=True
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.order_by_id,
            methods=["GET"],
            response_model=Order,
            responses={
                200: {"model": Order},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200,
            response_model_exclude_none=True
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create,
            methods=["POST"],
            response_model=Order,
            response_model_by_alias=True,
            responses={
                201: {"model": Order},
                409: {"model": ObjectDuplicated}
            },
            status_code=201,
            response_model_exclude_none=True
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.update,
            methods=["PUT"],
            response_model=Order,
            responses={
                200: {"model": Order},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200,
            response_model_exclude_none=True
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.delete,
            methods=["DELETE"],
            response_model=None,
            responses={
                204: {"model": None},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=204,
            response_model_exclude_none=True
        )

        self._order_case = order_case
    
    ## get_current_user é admin ou client?
    async def orders(self, db=Depends(get_db), current_user=Depends(get_current_user)):
        return self._order_case(db).get_all()

    async def order_by_id(self, id: UUID, db=Depends(get_db), current_user=Depends(get_current_user)):
        return self._order_case(db).get_by_id(id)

    async def create(self, order: Order, db=Depends(get_db), current_user=Depends(get_current_user)):
        return self._order_case(db).create(order)

    async def update(self, id: UUID, order: Order, db=Depends(get_db), current_user=Depends(get_current_user)):
        return self._order_case(db).update(id, order)

    async def delete(self, id: UUID, db=Depends(get_db), current_user=Depends(get_current_user)):
        self._order_case(db).delete(id)
    


class ComboController:
    pass
    # Define the ComboController here (e.g., CRUD operations)