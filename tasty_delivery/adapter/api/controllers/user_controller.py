from typing import List

from fastapi import APIRouter

from tasty_delivery.adapter.api.models.user import User as UserSchema
from tasty_delivery.core.application.use_cases.user_case import UserCase


class UserController:

    def __init__(self, user_case: UserCase):
        self.router = APIRouter(tags=["Users"], prefix='/users')
        self.router.add_api_route(
            path="/",
            endpoint=self.users,
            methods=["GET"],
            response_model=List[UserSchema],
            status_code=200
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create,
            methods=["POST"],
            response_model=UserSchema,
            status_code=201
        )

        self._user_case = user_case

    async def users(self):
        return self._user_case.get_users()

    async def create(self, user: UserSchema):
        return self._user_case.create(user)
