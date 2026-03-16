## n8n Workflow Logic: 
### The Orchestration Loop

**Trigger Node:** A Webhook or Cron job starts the process when a new technical spec is uploaded (e.g., to a GitHub repo or Google Drive).

**Agent 1 (HTTP Request Node):** Calls requirements_architect.py. It sends the raw spec and receives the Requirement JSON.

**Condition Node (The "Bifurcation" Gate):** Checks if the requirements are clear. If "Ambiguous," it sends a Slack/Email alert to the human supervisor. If "Clear," it proceeds.

**Agent 2 (HTTP Request Node):** Calls test_strategy_planner.py. It sends the Requirement JSON and receives the Strategy Map.

**Agent 3 (HTTP Request Node):** Calls sdet_automation_agent.py. It uses the Strategy Map and a RAG-connected vector database to generate the Pytest Script.

**Execution Node:** Pushes the generated code to a temporary environment (like a GitHub Action or a Docker container) for a sanity run.

# Workflow Orchestration (n8n) ⚙️

This project utilizes **n8n** as the central nervous system to coordinate the Multi-Agent System (MAS). 

### Key Logic Gates:
- **State Management**: Ensures that Agent 3 does not begin code generation until Agent 2 has finalized the network topology.
- **Human-in-the-Loop (HITL)**: If Agent 1 identifies a "High Risk" or "Ambiguous" requirement, the workflow pauses for an Orchestration Supervisor's approval via a Slack notification.
- **Feedback Loop**: If Agent 3's generated code fails a linting check, the error logs are fed back to the LLM for self-correction (Auto-Healing).
