from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from adapter.database.db import get_db
from core.application.use_cases.order.order_case import OrderCase
from core.domain.entities.order import OrderOUT, OrderIN, OrderUpdate
from core.domain.exceptions.exception_schema import ObjectNotFound, ObjectDuplicated

from security import get_current_user

class OrderController:
    
    def __init__(self, order_case: OrderCase = None):
        self.router = APIRouter(tags=["Orders"], prefix="/orders")
        self.router.add_api_route(
            path="/",
            endpoint=self.orders,
            methods=["GET"],
            response_model=List[OrderOUT],
            status_code=200,
            response_model_exclude_none=True
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.order_by_id,
            methods=["GET"],
            response_model=OrderOUT,
            responses={
                200: {"model": OrderOUT},
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
            response_model=OrderOUT,
            response_model_by_alias=True,
            responses={
                201: {"model": OrderOUT},
                409: {"model": ObjectDuplicated}
            },
            status_code=201,
            response_model_exclude_none=True
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.update,
            methods=["PUT"],
            response_model=OrderOUT,
            responses={
                200: {"model": OrderOUT},
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
    
    async def orders(self, db=Depends(get_db)):
        return self._order_case(db).get_all()

    async def order_by_id(self, id: UUID, db=Depends(get_db)):
        return self._order_case(db).get_by_id(id)

    async def order_by_client(self, client_id: UUID, db=Depends(get_db)):
        return self._order_case(db).get_by_client(client_id)

    async def create(self, order: OrderIN, db=Depends(get_db)):
        return self._order_case(db).create(order)

    async def update(self, id: UUID, order: OrderUpdate, db=Depends(get_db)):
        return self._order_case(db).update(id, order)

    async def delete(self, id: UUID, db=Depends(get_db)):
        self._order_case(db).delete(id)
