import os
import json
from typing import Dict
from openai import OpenAI 

class TestStrategyPlanner:
    """
    Agent 2: Cognitive layer that transforms structured requirements into 
    an executable test strategy, including topology and performance parameters.
    """
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4-turbo-preview"

    def _get_system_prompt(self) -> str:
        """
        Defines the logic for risk-based prioritization and infrastructure mapping.
        """
        return """
        You are a Principal Software Quality Engineer specializing in Multi-Cloud Networking.
        Your objective is to ingest a JSON Requirement Map and generate a detailed Test Strategy.
        
        LOGIC CONSTRAINTS:
        1. PRIORITIZATION: Rank test cases (P0-P3) based on system impact and failure risk.
        2. TOPOLOGY: Identify required network architecture (VPCs, Gateways, Tunnel Endpoints).
        3. RELIABILITY: Define specific parameters for long-duration (Soak/Spike) tests if stability is a requirement.
        4. VENDOR INTEROP: Specify hardware/software versions required for cross-vendor validation.
        
        OUTPUT FORMAT: Strictly valid JSON. Ensure the schema is optimized for downstream automation agents.
        """

    def generate_strategy_map(self, requirement_map: Dict) -> Dict:
        """
        Processes the Requirement Map and returns the Strategy Map.
        """
        try:
            prompt_content = f"Generate a technical strategy for the following requirements: {json.dumps(requirement_map)}"
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": prompt_content}
                ],
                response_format={"type": "json_object"}
            )
            
            return json.loads(response.choices[0].message.content)

        except Exception as e:
            # In production, use structured logging here
            print(f"Error in Strategy Planner Agent: {e}")
            return {}

# --- Example Execution (For local testing) ---
if __name__ == "__main__":
    # Ensure LLM_API_KEY is set in your environment variables
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        raise ValueError("LLM_API_KEY environment variable is not set.")

    planner = TestStrategyPlanner(api_key=api_key)
    
    # Generic requirement input
    sample_input = {
      "project_id": "MCN-EAA-STACK-01",
      "features": [
        {
          "name": "High Availability Tunneling",
          "priority": "P0",
          "type": "Automated",
          "context": "Must sustain traffic during gateway failover within 30s."
        }
      ]
    }
    
    strategy = planner.generate_strategy_map(sample_input)
    print(json.dumps(strategy, indent=2))
