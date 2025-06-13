from agno.agent import Agent
from agno.memory.v2.memory import  Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools

from config.model_config import ClaudeConfig
from agno.tools.yfinance import YFinanceTools

claudeConfig = ClaudeConfig()
claude_model = Claude(id=claudeConfig.model_id, api_key=claudeConfig.api_key)

memory = Memory(
    model=claude_model,
    db=SqliteMemoryDb(table_name="user_memory", db_file="tmp/agent.db"),
    delete_memories=True,
    clear_memories=True,
)
agent = Agent(
    model=Claude(id=claudeConfig.model_id, api_key=claudeConfig.api_key),
    name="Level 3 Agent",
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    user_id="sai",
    instructions=[
        "use tables to display data",
        "Include sources in your response",
        "Only include the report in your response. No other text.",
    ],
    memory=memory,
    enable_agentic_memory=True,
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        "My favourite stocks are MSTR, AAPL and TSLA",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    agent.print_response(
        "Can you compare my favourite stocks ?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )