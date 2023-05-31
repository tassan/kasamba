from typing import Any

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    """Base response model."""
    message: str = Field(..., example="Success")
    data: Any = Field(..., example=None)
