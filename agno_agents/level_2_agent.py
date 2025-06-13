from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType
from config.model_config import ClaudeConfig
from config.model_config import OpenAIConfig

claudeConfig = ClaudeConfig()
openaiConfig = OpenAIConfig()

kb = UrlKnowledge(
     urls=["https://docs.agno.com/introduction.md"],
     vector_db= LanceDb(
         uri="tmp/lancedb",
         table_name="agno_docs",
         search_type=SearchType.hybrid,
         embedder=OpenAIEmbedder(id="text-embedding-3-small", api_key= openaiConfig.api_key, dimensions=1536),
     ),
   )

storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="Level 2 Agent",
    model=Claude(id=claudeConfig.model_id, api_key=claudeConfig.api_key),
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=kb,
    storage=storage,
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    agent.print_response("What is Agno?", stream=True)