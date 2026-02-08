# backend/agents/base_agent.py
from typing import Dict, Any, List
import json
from datetime import datetime

def fake_llm(prompt: str) -> dict:
    """Mock LLM that returns structured data based on the prompt."""
    if "research" in prompt.lower():
        return {
            "themes": ["Theme 1", "Theme 2"],
            "pain_points": ["Pain point 1", "Pain point 2"],
            "personas": ["Persona 1", "Persona 2"]
        }
    elif "prioritize" in prompt.lower():
        return {
            "prioritized_features": [
                {"id": "1", "title": "Feature 1", "rice_score": 45.5},
                {"id": "2", "title": "Feature 2", "rice_score": 38.2}
            ]
        }
    elif "spec" in prompt.lower():
        return {
            "prd": {
                "title": "Sample PRD",
                "overview": "This is a sample PRD",
                "objectives": ["Objective 1", "Objective 2"],
                "user_stories": [
                    {"as_a": "user", "i_want": "to do X", "so_that": "I can achieve Y"}
                ],
                "acceptance_criteria": [
                    {"given": "condition", "when": "action", "then": "result"}
                ]
            }
        }
    elif "task" in prompt.lower():
        return {
            "tasks": [
                {
                    "title": "Implement feature X",
                    "description": "Detailed description",
                    "estimated_hours": 8.0
                }
            ],
            "handoff": {
                "summary": "Handoff document",
                "technical_notes": "Important notes for implementation",
                "created_at": datetime.utcnow().isoformat()
            }
        }
    return {"error": "No matching response pattern"}