# backend/agents/prioritization_agent.py
from typing import List, Dict, Any
from ..models.feature import Feature
from .base_agent import fake_llm

class PrioritizationAgent:
    def prioritize_features(self, features: List[Feature]) -> List[Dict[str, Any]]:
        # In a real implementation, this would use the RICE framework
        prompt = f"""
        Prioritize these features using the RICE framework:
        {[f.title for f in features]}
        
        Return JSON with: prioritized_features[]
        """
        
        result = fake_llm(prompt)
        return result.get("prioritized_features", [])