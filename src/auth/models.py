from pydantic import BaseModel, EmailStr, SecretStr


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr


class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr


class RefreshToken(BaseModel):
    refresh_token: str


class ResetPassword(BaseModel):
    email: EmailStr
    token: str

