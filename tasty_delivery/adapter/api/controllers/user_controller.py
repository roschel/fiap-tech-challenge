from typing import List

from fastapi import APIRouter

from tasty_delivery.core.domain.entities.user import User as User
from tasty_delivery.core.application.use_cases.user_case import UserCase
from tasty_delivery.core.domain.exceptions.user_exception import UserNotFound


class UserController:

    def __init__(self, user_case: UserCase):
        self.router = APIRouter(tags=["Users"], prefix='/users')
        self.router.add_api_route(
            path="/",
            endpoint=self.users,
            methods=["GET"],
            response_model=List[User],
            status_code=200
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create,
            methods=["POST"],
            response_model=User,
            responses={
                201: {"model": User},
                409: {"model": UserNotFound}
            },
            status_code=201
        )

        self._user_case = user_case

    async def users(self):
        return self._user_case.get_users()

    async def create(self, user: User):
        return self._user_case.create(user)
