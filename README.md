# Agentic-SQA-Orchestrator
This is the "elevator pitch" for your project. Based on your Strategic Initiative, it should summarize how you use an Agentic AI workflow to automate the SQA lifecycle from requirements analysis to production-ready execution
## Overview
This framework is an end-to-end Agentic AI workflow designed to automate the full Software Quality Assurance (SQA) lifecycle. By orchestrating specialized LLM-based agents via LangFlow and n8n, the system transitions the QA process from manual requirement analysis to autonomous, production-ready test execution.
### Strategic Impact
  **Accelerated Delivery:** 
    Achieved a 60% reduction in release cycles by integrating automated quality gates.
  **Predictive Reliability:** 
    Successfully identified critical memory leaks (post-48 hours) and session flapping through automated 5-day soak and spike tests.
  **High-Fidelity Scripting:** 
    Utilizes Retrieval-Augmented Generation (RAG) to produce executable Python scripts that maintain a 95% automation success rate.
  **Resource Optimization:** 
    Scaled from a founding role to a high-performing team by positioning engineers as Orchestration Supervisors.

## System Architecture
The framework operates as a decentralized network of autonomous agents coordinated by a central orchestration engine.
**Orchestration Layer:** Uses n8n to manage the state machine, decision branching, and feedback loops between agents.
**Intelligence Layer:** Powered by LangFlow, defining the specific RAG (Retrieval-Augmented Generation) chains and prompt logic.
**Execution Layer:** Leverages Antigravity to run generated Python scripts within a secure, sandboxed environment.

### The Agents 
Each agent is a specialized entity designed to handle one specific phase of the quality lifecycle.
#### 1. Requirements Architect
This agent acts as the "translator" for the system. It ingests technical documents—like PRDs, API specifications, or design docs—and outputs a structured JSON schema that defines exactly what needs to be tested. This ensures that the downstream agents have a single source of truth for the product's behavior.

## Documentation
- [Agent 1: Requirements Architect](./docs/requirements_architect.md)
- [Agent 2: Test Strategy Planner](./docs/test_strategy_planner.md)
- [Agent 3: SDET Automation Agent](./docs/sdet_automation_agent.md)

## Quick Start & Installation
This project is designed to run as a modular Python-based Multi-Agent System. You can run individual agents via the CLI or orchestrate them through a workflow engine like n8n.

1. Prerequisites
Python 3.10+
An OpenAI API Key (or Gemini API Key with minor configuration changes in the agents)
(Optional) n8n installed locally or via Cloud for workflow orchestration.

2. Setup
Clone the repository and install the required dependencies:

git clone https://github.com/your-username/Agentic-SQA-Orchestrator.git
cd Agentic-SQA-Orchestrator
pip install -r requirements.txt

3. Environment Configuration
Create a .env file in the root directory to store your credentials securely:
touch .env
LLM_API_KEY=your_api_key_here   <--- in env file

4. Running the Agents
You can execute the agents independently to see the transformation of data through the pipeline.

Step 1: Parse Requirements
python requirements_architect.py

Outputs a structured JSON Requirement Map from a sample technical specification.

Step 2: Generate Strategy
python test_strategy_planner.py

Processes the Requirement Map to produce a risk-based Strategy Map and network topology.

Step 3: Generate Automation Code
python sdet_automation_agent.py

Utilizes RAG-logic to generate executable Pytest scripts based on the Strategy Map.

### Orchestration Logic (n8n)
To run the full autonomous loop:
Import the provided workflow JSON (to be added to /orchestration folder).
Configure the HTTP Request Nodes to point to your local agent scripts or hosted endpoints.
Trigger the workflow to see the end-to-end flow from Spec -> Code.
