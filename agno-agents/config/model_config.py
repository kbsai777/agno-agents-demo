from dotenv import load_dotenv
import os

load_dotenv()


class ClaudeConfig:
    """
    Configuration class for Claude models.
    """

    def __init__(self, model_id: str = None, api_key: str = None):
        self.model_id = os.getenv("ANTHROPIC_MODEL_ID", model_id) or model_id
        self.api_key = os.getenv("ANTHROPIC_API_KEY", api_key) or api_key
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set.")
        if not self.model_id:
            raise ValueError("ANTHROPIC_MODEL_ID environment variable is not set.")

class OpenAIConfig:
    """
    Configuration class for OpenAI models.
    """

    def __init__(self, model_id: str = None, api_key: str = None):
        self.model_id = os.getenv("OPENAI_MODEL_ID", model_id) or model_id
        self.api_key = os.getenv("OPENAI_API_KEY", api_key) or api_key
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        if not self.model_id:
            raise ValueError("OPENAI_MODEL_ID environment variable is not set.")