from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.security import OAuth2PasswordRequestForm

from core.domain.value_objects.auth import Auth
from security import Token, authenticate_user, AuthenticationError, handle_user_signup, \
    handle_client_signup


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
            request: Request,
            cpf: Annotated[str, Form()],
            nome: Annotated[str, Form()],
            email: Annotated[str, Form()],
            admin: Annotated[bool, Form()] = False,
            password: Annotated[str, Form()] = None
    ):
        auth = Auth(cpf=cpf, nome=nome, email=email, admin=admin, password=password)
        if auth.admin:
            token = request.headers.get('Authorization')
            if not token:
                raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg='Não autorizado')
            else:
                return handle_user_signup(auth, token)
        else:
            return handle_client_signup(auth)
