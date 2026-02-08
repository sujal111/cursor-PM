# backend/models/feedback.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from enum import Enum

class FeedbackType(str, Enum):
    USER_FEEDBACK = "user_feedback"
    SUPPORT_TICKET = "support_ticket"
    INTERVIEW = "interview"
    SURVEY = "survey"

class FeedbackItem(BaseModel):
    id: str
    content: str
    feedback_type: FeedbackType
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: dict = Field(default_factory=dict)
    user_id: Optional[str] = None