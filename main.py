from fastapi import FastAPI, APIRouter

from src.routers import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
