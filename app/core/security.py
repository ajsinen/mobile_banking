from datetime import datetime, timedelta, UTC
from fastapi import HTTPException
import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from starlette import status

from app.core.config import settings

ph = PasswordHasher()


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return ph.verify(
            hashed_password,
            plain_password
        )
    except VerifyMismatchError:
        return False


def create_access_token(user_id: str, role: int) -> str:
    expire = datetime.now(UTC) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": user_id,
        "role": role,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(detail="Signature expired. Please log in again.", status_code=status.HTTP_401_UNAUTHORIZED)

    except jwt.InvalidTokenError:
        raise HTTPException(detail="Invalid token", status_code=status.HTTP_401_UNAUTHORIZED)
