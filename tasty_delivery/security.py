from datetime import timedelta, datetime

from fastapi import status, Security, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError

from adapter.database.db import get_db
from core.domain.entities.client import Client
from core.domain.entities.user import User
from core.domain.exceptions.exception import ObjectNotFound, DuplicateObject
from core.domain.value_objects.auth import Auth
from core.domain.value_objects.client_auth import ClientAuth
from logger import logger
from settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer_token = HTTPBearer()

EXPIRATION_ERROR = "Credencial expirada"
CREDENTIAL_ERROR = "Não foi possível validar o token"


class AuthenticationError(HTTPException):
    def __init__(self, status_code: int, msg):
        super(AuthenticationError, self).__init__(status_code=status_code, detail=msg)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    is_anonymous: bool = False
    scopes: list[str] = []

def get_current_user(token=Security(bearer_token)):
    from core.application.use_cases.user.user_case import UserCase
    from core.application.use_cases.client.client_case import ClientCase

    try:
        payload = jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except AttributeError:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    except ExpiredSignatureError:
        logger.warning(EXPIRATION_ERROR)
        raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg=EXPIRATION_ERROR)

    except (JWTError, ValidationError):
        logger.warning(CREDENTIAL_ERROR)
        raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg=CREDENTIAL_ERROR)

    username: str = payload.get("sub")
    if not username:
        username = "anonymous_user"
        is_anonymous = True
        #raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg=CREDENTIAL_ERROR)
    else:
        is_anonymous = False

    token_scopes = payload.get("scopes", [])
    token_data = TokenData(scopes=token_scopes, username=username, is_anonymous=is_anonymous)

    if 'client' in token_scopes:
        user = ClientCase(next(get_db())).get_by_cpf(cpf=token_data.username)
    else:
        user = UserCase(next(get_db())).get_by_username(user_name=token_data.username)
    if not user and not token_data.is_anonymous:
        logger.warning(CREDENTIAL_ERROR)
        raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg=CREDENTIAL_ERROR)
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def get_token(user):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": user.scopes},
        expires_delta=access_token_expires,
    )
    return Token(**{"access_token": access_token, "token_type": "bearer"})


def authenticate_user(form_data) -> Token:
    from core.application.use_cases.user.user_case import UserCase
    from core.application.use_cases.client.client_case import ClientCase

    if form_data.scopes and 'client' in form_data.scopes:
        if form_data.username:
            user = ClientCase(next(get_db())).get_by_cpf(form_data.username)
            user = ClientAuth(**user.model_dump(), username=user.cpf)
        else:
            user = ClientAuth(cpf="anonymous_user")
    else:
        user = UserCase(next(get_db())).get_by_username(form_data.username)

        if not user or not verify_password(form_data.password, user.hashed_password):
            raise ObjectNotFound(status_code=400, msg="Usuário ou senha incorretos")

    return get_token(user)


def handle_user_signup(user, token):
    from core.application.use_cases.user.user_case import UserCase

    current_user = get_current_user(token.split(' ')[1])

    result = UserCase(next(get_db()), current_user).get_by_cpf(user.cpf)
    if result:
        raise DuplicateObject("Usuário já existente na base de dados", 409)
    else:
        user = User(**user.model_dump(), username=user.email)
        user = UserCase(next(get_db()), current_user).create(user)

        return get_token(user)


def handle_client_signup(user: Auth):
    from core.application.use_cases.client.client_case import ClientCase

    client = ClientCase(next(get_db())).get_by_cpf(user.cpf)

    if client:
        raise DuplicateObject("Cliente já existente na base de dados", 409)
    else:
        user = Client(**user.model_dump())
        user = ClientCase(next(get_db())).create(user)

        return get_token(ClientAuth(**user.model_dump(), username=user.cpf))


def has_permission(permission):
    def decorator(func):
        def wrapped_function(*args, **kwargs):
            if 'client' in permission or 'login' in permission:
                return func(*args, **kwargs)

            use_case = args[0]
            current_user = use_case.current_user

            if bool(set(permission) & set(current_user.scopes)):
                return func(*args, **kwargs)
            else:
                raise AuthenticationError(status_code=status.HTTP_403_FORBIDDEN, msg="Acesso negado")

        return wrapped_function

    return decorator
