from typing import List

from fastapi import APIRouter, Depends

from tasty_delivery.adapter.database.db import get_db
from tasty_delivery.core.application.use_cases.user.user_case import UserCase
from tasty_delivery.core.domain.entities.user import User as User
from tasty_delivery.core.domain.exceptions.exception_schema import ObjectNotFound, ObjectDuplicated


class UserController:

    def __init__(self, user_case: UserCase = None):
        self.router = APIRouter(tags=["Users"], prefix='/users')
        self.router.add_api_route(
            path="/",
            endpoint=self.users,
            methods=["GET"],
            response_model=List[User],
            status_code=200
        )
        self.router.add_api_route(
            path="/{id}",
            endpoint=self.user_by_id,
            methods=["GET"],
            response_model=User,
            responses={
                200: {"model": User},
                404: {"model": ObjectNotFound},
                409: {"model": ObjectDuplicated}
            },
            status_code=200
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create,
            methods=["POST"],
            response_model=User,
            responses={
                201: {"model": User},
                409: {"model": ObjectDuplicated}
            },
            status_code=201
        )

        self._user_case = user_case

    async def users(self, db=Depends(get_db)):
        return self._user_case(db).get_users()

    async def user_by_id(self, id: int, db=Depends(get_db)):
        return self._user_case(db).get_user_by_id(id)

    async def create(self, user: User, db=Depends(get_db)):
        return self._user_case(db).create(user)
