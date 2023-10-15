from typing import Annotated

from fastapi import APIRouter, Form

from core.domain.value_objects.auth import Auth
from security.base import Token
from security.client_security import authenticate_client, signup_client


class AuthClientController:
    def __init__(self):
        self.router = APIRouter(tags=["Authentication for Clients"], prefix='/auth-client')
        self.router.add_api_route(
            path="/login",
            endpoint=self.login,
            methods=["POST"],
            response_model=Token,
            status_code=200
        )
        self.router.add_api_route(
            path="/signup",
            endpoint=self.signup,
            methods=["POST"],
            response_model=Token,
            status_code=200
        )

    async def login(self, cpf: Annotated[str, Form()]):
        return authenticate_client(cpf)

    async def signup(self,
                     cpf: Annotated[str, Form()],
                     nome: Annotated[str, Form()],
                     email: Annotated[str, Form()]):
        auth = Auth(cpf=cpf, nome=nome, email=email)
        return signup_client(auth)
