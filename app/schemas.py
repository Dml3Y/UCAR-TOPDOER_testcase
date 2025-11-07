from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class IncidentStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IncidentSource(str, Enum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"

# Базовая схема инцидента
class IncidentBase(BaseModel):
    description: str
    source: IncidentSource

# Схема для создания инцидента
class IncidentCreate(IncidentBase):
    pass

# Схема для обновления статуса
class IncidentStatusUpdate(BaseModel):
    status: IncidentStatus

# Полная схема инцидента (для ответов)
class Incident(IncidentBase):
    id: int
    status: IncidentStatus
    created_at: datetime

    class Config:
        from_attributes = True