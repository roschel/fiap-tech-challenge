from datetime import timedelta, datetime

from fastapi import status, Security, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError

from adapter.database.db import get_db
from core.application.use_cases.user.user_case import UserCase
from core.domain.exceptions.exception import ObjectNotFound
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
    scopes: list[str] = []


def get_current_user(token=Security(bearer_token)):
    try:
        payload = jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            pass
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except ExpiredSignatureError:
        logger.warning(EXPIRATION_ERROR)
        raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg=EXPIRATION_ERROR)

    except (JWTError, ValidationError):
        logger.warning(CREDENTIAL_ERROR)
        raise AuthenticationError(status_code=status.HTTP_401_UNAUTHORIZED, msg=CREDENTIAL_ERROR)

    user = UserCase(next(get_db())).get_user_by_username(user_name=token_data.username)
    if not user:
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


def authenticate_user(form_data) -> Token:
    user = UserCase(next(get_db())).get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise ObjectNotFound(status_code=400, msg="Usuário ou senha incorretos")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return Token(**{"access_token": access_token, "token_type": "bearer"})
