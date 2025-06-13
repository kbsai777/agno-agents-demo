
from agno.agent import  Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from config.model_config import ClaudeConfig


config = ClaudeConfig()
anthropic_model = Claude(id = config.model_id, api_key= config.api_key)

agent = Agent(
    name="Level 1 Agent",
    description="A basic agent that can use the yfinance tool to fetch stock data.",
    model=anthropic_model,
    tools=[YFinanceTools()],
    instructions= "Use tables to display data. Don't include any other text.",
    markdown= True,
    show_tool_calls= True
)

agent.print_response("What is the current stock price of MSTR?" , stream=True)