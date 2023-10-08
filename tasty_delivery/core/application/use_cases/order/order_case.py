from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from core.application.use_cases.product.iproduct_case import IProductCase
from adapter.repositories.order_repository import OrderRepository
from core.application.use_cases.client.iclient_case import IClientCase
from core.application.use_cases.order.iorder_case import IOrderCase
from core.domain.entities.order import Order, Combo

from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound

from logger import logger
from security import has_permission

class OrderCase(IOrderCase):

    def __init__(self, db=None):
        self.repository = OrderRepository(db)

    @has_permission(permission=['client'])
    def create_order(self, order: Order):
        try:
            order.id = uuid4()
            # Set other properties of the order
            return self.repository.create(order)
        except IntegrityError:
            msg = "Order already exists in the database"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)
    def create_combo(self, combo: Combo):
        try:
            combo.id = uuid4()
            # Set other properties of the combo
            return self.repository.create_combo(combo)
        except IntegrityError:
            msg = "Combo already exists in the database"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)
