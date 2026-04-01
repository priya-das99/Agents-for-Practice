from agents import Agent
from tools.budget_tool import budget_agent
from tools.investment_tool import investment_agent
from tools.risk_tool import risk_agent
from schemas.finance_models import FinanceResponse

orchestrator_agent = Agent(
    name="finance_orchestrator",
    model="gpt-4.1-mini",
    instructions="""
You are a personal finance assistant.

You MUST use tools to answer:
- Budget questions → use budget tool
- Investment questions → use investment tool
- Risk analysis → use risk tool

If user asks multiple things, call multiple tools.

Do NOT answer on your own.
""",
    tools=[
        budget_agent.as_tool(
            tool_name="create_budget",
            tool_description="Create monthly budget plan"
        ),
        investment_agent.as_tool(
            tool_name="suggest_investments",
            tool_description="Suggest investment options"
        ),
        risk_agent.as_tool(
            tool_name="analyze_risk",
            tool_description="Analyze financial risk"
        ),
    ],
)





synthesizer_agent = Agent(
    name="finance_synthesizer",
    model="gpt-4.1-mini",
    instructions="""
You are a financial data formatter.

Combine all tool outputs into ONE clean JSON.

Follow the schema strictly.

Do NOT add extra text.
""",
    output_type=FinanceResponse  # 🔥 THIS IS THE MAGIC
)