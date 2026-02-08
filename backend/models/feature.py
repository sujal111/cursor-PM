# backend/models/feature.py
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class FeatureStatus(str, Enum):
    BACKLOG = "backlog"
    PRIORITIZED = "prioritized"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Feature(BaseModel):
    id: str
    title: str
    description: str
    status: FeatureStatus = FeatureStatus.BACKLOG
    rice_score: Optional[float] = None
    reach: int = 0
    impact: int = 0
    confidence: int = 0
    effort: int = 0
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())