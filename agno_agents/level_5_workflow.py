from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow
from config.model_config import OpenAIConfig

open_ai_config= OpenAIConfig()
class CacheWorkflow(Workflow):
    # Add agents or teams as attributes on the workflow
    agent = Agent(model=OpenAIChat(id=open_ai_config.model_id, api_key=open_ai_config.api_key))

    # Write the logic in the `run()` method
    def run(self, message: str) -> Iterator[RunResponse]:
        logger.info(f"Checking cache for '{message}'")
        # Check if the output is already cached
        cached_response = self.session_state.get(message)
        print(f"Cached response: {cached_response}")
        if cached_response:
            logger.info(f"Cache hit for '{message}'")
            # Create a proper RunResponse with the cached content
            yield RunResponse(
                run_id=self.run_id, content=cached_response
            )
            return

        logger.info(f"Cache miss for '{message}'")
        # Run the agent and yield the response
        for response in self.agent.run(message, stream=True):
            yield response

        # Cache the output after response is yielded
        self.session_state[message] = self.agent.run_response.content


if __name__ == "__main__":
    workflow = CacheWorkflow()
    # Run workflow (this is takes ~1s)
    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)
    # Run workflow again (this is immediate because of caching)
    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)

    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)