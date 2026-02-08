# backend/agents/spec_agent.py
from typing import Dict, Any
from ..models.spec import PRD, UserStory, AcceptanceCriteria
from .base_agent import fake_llm

class SpecGenerationAgent:
    def generate_spec(self, feature: Dict[str, Any]) -> PRD:
        prompt = f"""
        Generate a Product Requirements Document for: {feature['title']}
        Include: overview, objectives, user stories, and acceptance criteria.
        """
        
        result = fake_llm(prompt)
        prd_data = result.get("prd", {})
        
        return PRD(
            title=prd_data.get("title", "Untitled PRD"),
            overview=prd_data.get("overview", ""),
            objectives=prd_data.get("objectives", []),
            user_stories=[
                UserStory(**us) for us in prd_data.get("user_stories", [])
            ],
            acceptance_criteria=[
                AcceptanceCriteria(**ac) for ac in prd_data.get("acceptance_criteria", [])
            ]
        )