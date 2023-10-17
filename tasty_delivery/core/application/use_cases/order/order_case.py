from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from adapter.database.models.order import Order as OrderDB
from adapter.repositories.order_repository import OrderRepository
from adapter.database.models.client import Client as ClientDB
from core.application.use_cases.order.iorder_case import IOrderCase
from core.domain.entities.order import OrderIN, OrderOUT, OrderUpdate


from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound

from logger import logger
from security import has_permission

class OrderCase(IOrderCase):

    def __init__(self, db=None):
        self.repository = OrderRepository(db)
        # self.current_client = current_client

    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, id):
        result = self.repository.get_by_id(id)
        if not result:
            msg = f"Pedido {id} não encontrado."
            logger.warning(msg)
            raise ObjectNotFound(msg, 404)
        return result
    
    def get_by_client(self, client_id):
        return self.repository.get_by_client(client_id)

    @has_permission(permission=['client'])
    def create(self, order: OrderIN) -> OrderOUT:
        try:
            order.id = uuid4()
            # order.created_by = self.current_client.id
            return self.repository.create(OrderDB(**vars(order)))
        except IntegrityError:
            msg = "Pedido já existente criado na base de dados."
            logger.warning(msg)
            raise DuplicateObject(msg, 409)
        
    @has_permission(permission=['client'])
    def update(self, id, new_values: OrderUpdate) -> OrderOUT:
        new_values.id = None
        # new_values.updated_by = self.current_client.id
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    @has_permission(permission=['client'])
    def delete(self, id):
        return self.repository.delete(id)
