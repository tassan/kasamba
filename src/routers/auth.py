from click import DateTime
from fastapi import APIRouter

from src.auth.models import *

router = APIRouter()


@router.post("/register")
async def register_user(user: UserRegister):
    return {"username": user.username, "email": user.email, "created_at": DateTime.now(), "is_email_verified": False}


@router.post("/login")
async def login_user(login: UserLogin):
    return {"user": login.email, "token": "token"}


@router.post("/logout")
async def logout_user():
    return {"message": "User logged out"}


@router.get("/me")
async def get_user():
    return {"message": "User details"}


@router.post("/refresh")
async def refresh_token(refresh: RefreshToken):
    return refresh


@router.post("/reset-password")
async def reset_password(reset: ResetPassword):
    if reset is None:
        return {"message": "Password reset failed"}

    return {"message": "Password reset"}
