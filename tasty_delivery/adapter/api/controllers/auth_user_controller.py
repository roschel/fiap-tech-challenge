from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from core.domain.value_objects.auth import Auth
from security.base import get_current_user, Token
from security.user_security import authenticate_user, handle_user_signup


class AuthController:
    def __init__(self):
        self.router = APIRouter(tags=["Authentication"], prefix='/auth')
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

    async def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        return authenticate_user(form_data)

    async def signup(
            self,
            cpf: Annotated[str, Form()],
            nome: Annotated[str, Form()],
            email: Annotated[str, Form()],
            admin: Annotated[bool, Form()] = False,
            password: Annotated[str, Form()] = None,
            current_user=Depends(get_current_user)
    ):
        auth = Auth(cpf=cpf, nome=nome, email=email, admin=admin, password=password)
        return handle_user_signup(auth, current_user)
