from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from security import Token, authenticate_user


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

    async def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        return authenticate_user(form_data)
