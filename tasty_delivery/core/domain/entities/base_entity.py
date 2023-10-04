from datetime import datetime

from pydantic import BaseModel, Field
from uuid import UUID


class Base(BaseModel):
    id: UUID = Field(None)
    is_active: bool = Field(True)
    is_deleted: bool = Field(False)
    created_at: datetime | None = Field(None)
    updated_at: datetime | None = Field(None)
