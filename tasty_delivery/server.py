from fastapi import FastAPI

from tasty_delivery.adapter.api.controllers.user_controller import UserController
from tasty_delivery.adapter.database.db import get_db
from tasty_delivery.core.application.use_cases.user_case import UserCase
from tasty_delivery.core.domain.entities.user import User

app = FastAPI()

# Users
route_controller = UserController(UserCase)
app.include_router(route_controller.router)


@app.on_event("startup")
async def populate_database():
    mock_user = [
        User(nome="João", cpf="11122233344", email="joao@email.com"),
        User(nome="Victor", cpf="2223334455", email="victor@email.com"),
        User(nome="Tais", cpf="33344455566", email="tais@email.com"),
        User(nome="Augusto", cpf="44455566677", email="augusto@email.com"),
    ]

    for user in mock_user:
        db = get_db()
        UserCase(next(db)).create(user)
