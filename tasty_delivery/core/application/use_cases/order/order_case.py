from sqlalchemy.exc import IntegrityError

from adapter.database.models.client import Client as ClientDB
from adapter.database.models.order import Order as OrderDB
from adapter.repositories.order_repository import OrderRepository
from core.application.use_cases.order.iorder_case import IOrderCase
from core.domain.entities.order import OrderIN, OrderOUT, OrderUpdate
from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound, InvalidStatus
from core.domain.value_objects.order_status import OrderStatus
from logger import logger
from security.base import has_permission


class OrderCase(IOrderCase):
    RECEBIDO = OrderStatus.RECEBIDO.name
    EM_PREPARACAO = OrderStatus.EM_PREPARACAO.name
    PRONTO = OrderStatus.PRONTO.name
    FINALIZADO = OrderStatus.FINALIZADO.name

    AVAILABLE_STATUS = (RECEBIDO, EM_PREPARACAO, PRONTO, FINALIZADO)

    def __init__(self,
                 db=None,
                 current_client: ClientDB = None,
                 current_user=None):
        self.repository = OrderRepository(db)
        self.current_client = current_client
        self.current_user = current_user

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
        result = self.repository.get_by_client(client_id)
        return result

    @has_permission(permission=['client'])
    def create(self, order: OrderIN) -> OrderOUT:
        client_id = self.current_client.id if self.current_client else None
        try:
            obj = OrderDB(
                **order.model_dump(mode='json'),
                client_id=client_id,
                status=OrderCase.RECEBIDO
            )

            return self.repository.create(obj)
        except IntegrityError:
            msg = "Pedido já existente criado na base de dados."
            logger.warning(msg)
            raise DuplicateObject(msg, 409)
        except Exception as e:
            raise e

    @has_permission(permission=['admin'])
    def update_status(self, id, status: str) -> OrderOUT:
        new_status = status.upper()

        if new_status not in OrderCase.AVAILABLE_STATUS:
            raise InvalidStatus(status_code=400, msg=f"Status {status} não é valido.")
        return self.repository.update_status(
            id,
            {"status": new_status, "updated_by": self.current_user.id}
        )

    @has_permission(permission=['client'])
    def update(self, id, new_values: OrderUpdate) -> OrderOUT:
        new_values.id = None
        new_values.updated_by = self.current_client.id
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    @has_permission(permission=['admin'])
    def delete(self, id):
        return self.repository.delete(id, self.current_client)
