# backend/models/spec.py
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime

class UserStory(BaseModel):
    as_a: str
    i_want: str
    so_that: str

class AcceptanceCriteria(BaseModel):
    given: str
    when: str
    then: str

class PRD(BaseModel):
    title: str
    overview: str
    objectives: List[str]
    user_stories: List[UserStory]
    acceptance_criteria: List[AcceptanceCriteria]
    technical_notes: str = ""

class Task(BaseModel):
    id: str
    title: str
    description: str
    status: str = "todo"
    depends_on: List[str] = Field(default_factory=list)
    estimated_hours: float = 0.0