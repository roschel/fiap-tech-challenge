from fastapi import FastAPI

from tasty_delivery.adapter.api.controllers.user_controller import UserController
from tasty_delivery.adapter.repositories.user_repository import UserRepository
from tasty_delivery.core.application.use_cases.user_case import UserCase

app = FastAPI()

# Users
user_repo = UserRepository()

route_controller = UserController(UserCase(user_repo))
app.include_router(route_controller.router)
