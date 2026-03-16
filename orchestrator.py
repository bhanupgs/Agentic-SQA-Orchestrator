import os
import json
from dotenv import load_dotenv

# Importing your agent classes
from requirements_architect import RequirementsArchitect
from test_strategy_planner import TestStrategyPlanner
from sdet_automation_agent import SDETAutomationAgent

# Load environment variables from .env
load_dotenv()

def run_sqa_orchestration_pipeline(tech_spec: str):
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        print("Error: LLM_API_KEY not found in environment.")
        return

    # Initialize Agents
    architect = RequirementsArchitect(api_key)
    planner = TestStrategyPlanner(api_key)
    sdet_agent = SDETAutomationAgent(api_key)

    print("---  Phase 1: Requirement Extraction ---")
    req_map = architect.generate_requirement_map(tech_spec)
    print("Requirement Map Generated Successfully.")

    print("\n---  Phase 2: Strategic Planning ---")
    strategy_map = planner.generate_strategy_map(req_map)
    print(f"Strategy mapped for Project: {strategy_map.get('strategy_id', 'Unknown')}")

    print("\n---  Phase 3: SDET Code Generation ---")
    # Using a sample RAG context for coding standards
    standards = "Use Pytest fixtures and log every assertion with internal_logger."
    automation_result = sdet_agent.generate_test_code(strategy_map, standards)
    
    print("\n--- Orchestration Complete ---")
    print("Generated Code Preview:")
    print(automation_result.get("code", "Code generation failed.")[:200] + "...")

if __name__ == "__main__":
    # Sample input representing a complex networking feature
    sample_spec = """
    Feature: Multi-Cloud Load Balancer. 
    Description: Must balance traffic between AWS and GCP instances using a Round Robin algorithm.
    Requirement: 100% uptime during peak loads and automatic health-check failover.
    """
    
    run_sqa_orchestration_pipeline(sample_spec)
