from datetime import datetime

from pydantic import BaseModel, Field


class Base(BaseModel):
    id: int = Field(None)
    is_active: bool = Field(True)
    is_deleted: bool = Field(False)
    created_at: datetime = Field(None)
    updated_at: datetime = Field(None)
