💰 Personal Finance Advisor Agent (OpenAI Agents SDK)
📌 Overview

This project is a multi-agent AI system built using the OpenAI Agents SDK. It acts as a Personal Finance Advisor that helps users:

📊 Create a monthly budget
📈 Get investment suggestions
⚠️ Analyze financial risk

It demonstrates the Agents-as-Tools pattern, where a central agent delegates tasks to specialized agents.
🧠 Architecture

User Input
   ↓
Orchestrator Agent (Decision Maker)
   ↓
-----------------------------------
| Budget Agent       (💰 Budget)   |
| Investment Agent   (📈 Advice)   |
| Risk Agent         (⚠️ Analysis) |
-----------------------------------
   ↓
Synthesizer Agent (📊 Structured Output)
   ↓
Final Response (Pydantic Object)

🧩 Components
🧠 Orchestrator Agent
Decides which agents (tools) to call
Understands user intent
Does NOT generate final answers

💰 Budget Agent
Creates budget using 50-30-20 rule
Outputs:
Needs
Wants
Savings
Provides financial tips

⚠️ Currently uses LLM-based estimation (not deterministic logic yet)

📈 Investment Agent
Suggests:
Emergency fund
Mutual funds (SIP)
Fixed deposits
Stocks (basic)
Focuses on beginner-friendly advice

⚠️ Risk Agent
Determines risk level (Low / Medium / High)
Identifies potential financial risks
Suggests safer alternatives

📊 Synthesizer Agent
Combines outputs from all agents
Enforces structured output using Pydantic schema
Produces clean final response

🧱 Tech Stack
Python (Async)
OpenAI Agents SDK
Pydantic (Structured Output Validation)

📁 Project Structure
finance-agent/
│
├── main.py
├── agents.py
│
├── tools/
│   ├── budget_tool.py
│   ├── investment_tool.py
│   └── risk_tool.py
│
├── schemas/
│   └── finance_models.py

🔐 Structured Output (Schema)

The system enforces structured output using Pydantic:

✅ Example Output
class FinanceResponse(BaseModel):
    budget: Budget
    investments: Investments
    risk: Risk

    {
  "budget": {
    "needs": 30000,
    "wants": 18000,
    "savings": 12000,
    "tips": ["..."]
  },
  "investments": {
    "emergency_fund": "...",
    "mutual_funds": ["..."],
    "fixed_deposits": ["..."],
    "stocks": ["..."],
    "notes": ["..."]
  },
  "risk": {
    "risk_level": "Medium",
    "reasons": ["..."],
    "warnings": ["..."],
    "safer_options": ["..."]
  }
}

⚙️ How It Works
User enters a financial query
Orchestrator analyzes intent
Calls relevant agents as tools
Each agent generates domain-specific output
Synthesizer merges outputs into structured schema
Final response is returned

⚠️ Current Limitations
❌ Budget logic is LLM-based (not exact calculation)
❌ No real-time financial data
❌ No user memory / personalization
❌ No external API integration

▶️ How to Run
 Create Python virtual Environment 
 python -m venv
 Activate the virtual environment
 .\venv\scripts\activate
Then run following command 
pip install -r requirements.txt
python main.py

💡 Example Input
I earn ₹50,000 per month. Suggest a budget, investments, and risk analysis.
