from datetime import timedelta
from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from logger import logger
from security import verify_password, create_access_token, Token
from settings import settings
from tasty_delivery.adapter.database.models.user import User as UserDB
from tasty_delivery.adapter.repositories.user_repository import UserRepository
from tasty_delivery.core.application.use_cases.user.iuser_case import IUserCase
from tasty_delivery.core.domain.entities.user import User


class UserCase(IUserCase):

    def __init__(self, db=None):
        self.repository = UserRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        result = self.repository.get_by_id(id)
        if not result:
            msg = f"Usuário {id} não encontrado"
            logger.warning(msg)
            raise ObjectNotFound(msg, 404)
        return result

    def create(self, obj: User) -> User:
        try:
            obj.id = uuid4()
            return self.repository.create(UserDB(**vars(obj)))
        except IntegrityError:
            msg = "Usuário já existente na base de dados"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)

    def update(self, id, new_values: User) -> User:
        new_values.id = None
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    def delete(self, id):
        return self.repository.delete(id)

    def authenticate_user(self, form_data) -> Token:
        user = self.repository.get_user_by_username(form_data.username)
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise ObjectNotFound(status_code=400, msg="Usuário ou senha incorretos")

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scopes": form_data.scopes},
            expires_delta=access_token_expires,
        )
        return Token(**{"access_token": access_token, "token_type": "bearer"})
