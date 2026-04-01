# Finance Planner Agent

`FinancePlannerAgent` is a small multi-agent personal finance demo built with the OpenAI Agents SDK. It takes a free-form finance question, routes the request to specialized agents, and returns a structured finance response.

The project currently focuses on three areas:

- Monthly budget suggestions
- Beginner-friendly investment ideas
- Basic financial risk analysis

## What It Does

The application uses an orchestrator agent to decide which specialist agents should respond to a user query:

- `budget_agent` creates a budget suggestion
- `investment_agent` suggests investment options
- `risk_agent` analyzes financial risk

Their outputs are then passed to a synthesizer agent, which converts the result into a validated Pydantic model.

## Architecture

```text
User Query
    |
    v
Orchestrator Agent
    |
    +--> Budget Tool
    +--> Investment Tool
    +--> Risk Tool
    |
    v
Synthesizer Agent
    |
    v
Structured FinanceResponse
```

## Project Structure

```text
FinancePlannerAgent/
|-- agent.py
|-- main.py
|-- readme.md
|-- requirements.txt
|-- schemas/
|   `-- finance_models.py
`-- tools/
    |-- budget_tool.py
    |-- investment_tool.py
    `-- risk_tool.py
```

## Data Model

The final output is validated against the `FinanceResponse` schema defined in `schemas/finance_models.py`.

```python
class FinanceResponse(BaseModel):
    budget: Budget
    investments: Investments
    risk: Risk
```

That response contains:

- `budget`: needs, wants, savings, and tips
- `investments`: emergency fund, mutual funds, fixed deposits, stocks, and notes
- `risk`: risk level, reasons, warnings, and safer options

## Requirements

- Python 3.10+
- An OpenAI API key

## Setup

1. Create a virtual environment:

```powershell
python -m venv venv
```

2. Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Set your API key:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

If you prefer a `.env` file, make sure your runtime loads it before execution.

## Run The Project

```powershell
python main.py
```

You will be prompted for a finance question such as:

```text
I earn 50000 per month. Suggest a budget, investment options, and a risk analysis.
```

## How The Flow Works

1. `main.py` collects the user query.
2. The orchestrator agent decides which tools to call.
3. Specialist agents produce domain-specific responses.
4. The synthesizer agent converts those outputs into a `FinanceResponse` object.
5. The result is printed in the console.

## Current Limitations

- No real-time market or banking data
- No long-term user memory or personalization
- Budget advice is prompt-driven, not rule-engine based
- Investment suggestions are educational, not professional financial advice

## Notes

- The file is currently named `readme.md`. If you want better GitHub rendering conventions, rename it to `README.md`.
- `python-dotenv` is listed in `requirements.txt`, but the current code does not explicitly call `load_dotenv()`.

## Example Use Case

This project is useful as a starter template for:

- OpenAI Agents SDK experiments
- Tool-routing demos
- Structured multi-agent outputs with Pydantic
- Beginner portfolio or budgeting assistant prototypes
