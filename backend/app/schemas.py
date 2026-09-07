# app/schemas.py
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from uuid import UUID

# Base properties shared across different schemas
class MonitorBase(BaseModel):
    url: HttpUrl
    interval_minutes: int
    is_active: bool = True

# Used when the React app sends data TO the API to create a new monitor
# (We don't expect the user to send an ID or created_at, so it just inherits the Base)
class MonitorCreate(MonitorBase):
    pass

# Used when the API sends data BACK to the React app
class MonitorResponse(MonitorBase):
    id: UUID
    created_at: datetime

    class Config:
        # This tells Pydantic to read data directly from the SQLAlchemy model
        from_attributes = True