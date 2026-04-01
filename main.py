import asyncio
import json
from agents import Runner
from agent import orchestrator_agent, synthesizer_agent

async def main():
    user_input = input("Enter your financial query: ")

    # Step 1: Run orchestrator
    orchestrator_result = await Runner.run(orchestrator_agent, user_input)

    # Step 2: Pass ALL outputs to synthesizer
    synthesizer_result = await Runner.run(
        synthesizer_agent,
        orchestrator_result.to_input_list()
    )

    print("\nFinal Structured Output:\n")
    print(synthesizer_result.final_output)
    print(synthesizer_result.budget.needs)
    print(synthesizer_result.investments.mutual_funds)
    print(synthesizer_result.risk.risk_level)


if __name__ == "__main__":
    asyncio.run(main())