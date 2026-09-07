# app/models.py
import uuid
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .database import Base

class Monitor(Base):
    __tablename__ = "monitors"

    # UUIDs are better than sequential IDs (1, 2, 3) for security so people can't guess your API endpoints
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)
    interval_minutes = Column(Integer, nullable=False, default=15)
    is_active = Column(Boolean, default=True)
    
    # Let the database handle the creation timestamp automatically
    created_at = Column(DateTime(timezone=True), server_default=func.now())