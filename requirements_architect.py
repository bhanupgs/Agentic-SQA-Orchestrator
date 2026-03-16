import os
import json
from typing import Dict
# Using a generic client structure for flexibility (OpenAI/Gemini/etc.)
from openai import OpenAI 

class RequirementsArchitect:
    """
    Agent 1: Ingests technical specifications and outputs structured 
    test requirements to drive the autonomous QA lifecycle[cite: 15].
    """
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4-turbo-preview" # Or "gemini-pro" via Vertex AI

    def get_system_prompt(self) -> str:
        """
        Defines the architectural logic for the agent.
        Ensures the output follows the schema defined in docs/requirements_architect.md.
        """
        return """
        You are a Senior SQA Requirements Architect with a Ph.D. in Computer Science.
        Your goal is to parse unstructured technical specifications and output a structured JSON Requirement Map.
        
        CRITICAL RULES:
        1. Identify functional modules and API endpoints.
        2. BIFURCATE: Determine if a requirement is 'Automated' (regression/API) or 'Manual' (exploratory)[cite: 15].
        3. TOPOLOGY: Define networking components (L2/L3 switches, cloud instances, tunnels) needed[cite: 15].
        4. ASSERTIONS: List critical success criteria for each feature.
        
        OUTPUT FORMAT: Strictly valid JSON only. No prose.
        """

    def generate_requirement_map(self, tech_spec_text: str) -> Dict:
        """
        Processes the input document and returns the structured JSON map.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.get_system_prompt()},
                    {"role": "user", "content": f"Analyze this spec: {tech_spec_text}"}
                ],
                response_format={"type": "json_object"}
            )
            
            # Parse the AI response into a Python dictionary
            requirement_map = json.loads(response.choices[0].message.content)
            return requirement_map

        except Exception as e:
            print(f"Error in Requirements Architect Agent: {e}")
            return {}

# --- Example Usage ---
if __name__ == "__main__":
    # In a real n8n/LangFlow workflow, this would be an environment variable
    ARCHITECT_API_KEY = os.getenv("LLM_API_KEY")
    
    architect = RequirementsArchitect(api_key=ARCHITECT_API_KEY)
    
    # Example raw input from a PRD or API doc [cite: 15]
    sample_spec = """
    Feature: IPsec Tunnel Stability. The system must establish a secure tunnel 
    between the AWS Gateway-V and the on-prem endpoint within 30 seconds. 
    Traffic must sustain zero packet loss during a 48-hour soak test.
    """
    
    # Execute the agent logic
    result = architect.generate_requirement_map(sample_spec)
    
    # Print the structured output intended for Agent 2 [cite: 14]
    print(json.dumps(result, indent=2))
