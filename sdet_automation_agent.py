import os
import json
from typing import Dict
from openai import OpenAI 

class SDETAutomationAgent:
    """
    Agent 3: Generates executable test scripts using RAG to align with 
    pre-defined coding standards and library patterns.
    """
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4-turbo-preview"

    def _get_system_prompt(self, coding_standards: str) -> str:
        """
        Sets the parameters for high-fidelity code generation.
        """
        return f"""
        You are an SDET Automation Engine. 
        Generate executable Python/Pytest code based on a provided Strategy Map.
        
        CODE GENERATION RULES:
        1. STANDARDS: Follow these library patterns: {coding_standards}
        2. FRAMEWORK: Use Pytest with modular fixtures.
        3. ROBUSTNESS: Include comprehensive error handling and logging.
        4. DOCUMENTATION: Include docstrings for every test case.
        
        OUTPUT FORMAT: Return a JSON object with a 'code' key containing the stringified script.
        """

    def generate_test_code(self, strategy_map: Dict, standards_context: str) -> Dict:
        """
        Generates production-ready test scripts.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._get_system_prompt(standards_context)},
                    {"role": "user", "content": f"Generate code for: {json.dumps(strategy_map)}"}
                ],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Code Generation Error: {e}")
            return {}

if __name__ == "__main__":
    api_key = os.getenv("LLM_API_KEY")
    agent = SDETAutomationAgent(api_key=api_key)
    
    # Logic: In a real app, 'standards_context' would be retrieved from a Vector DB (RAG)
    standards = "Use 'test_gateway' fixture. Assertions must use custom_logger.info()."
    strategy = {"case": "Gateway_Ping", "priority": "P0"}
    
    generated = agent.generate_test_code(strategy, standards)
    print(generated.get("code", "Generation Failed"))
