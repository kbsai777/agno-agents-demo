from typing import List
from rich.pretty import pprint
from pydantic import BaseModel, Field
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno_agents.config.model_config import OpenAIConfig

openaiConfig = OpenAIConfig()

class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(
        ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")

# Agent that uses JSON mode
json_mode_agent = Agent(
    model=OpenAIChat(id=openaiConfig.model_id, api_key=openaiConfig.api_key),
    description="You write movie scripts.",
    response_model=MovieScript,
    use_json_mode=True,
)
json_mode_agent.print_response("New York")

# Agent that uses structured outputs
structured_output_agent = Agent(
    model=OpenAIChat(id=openaiConfig.model_id, api_key=openaiConfig.api_key),
    description="You write movie scripts.",
    response_model=MovieScript,
)

structured_output_agent.print_response("New York")