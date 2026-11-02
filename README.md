# Agno Agents Demo

A level-by-level exploration of AI agent patterns using the [Agno](https://www.agno.com) framework — progressing from a single tool-using agent to multi-agent teams and stateful workflows. Built with Python, using OpenAI and Anthropic Claude models.

## The Levels

| File | What it demonstrates |
|---|---|
| `agno_agents/level_1_agent.py` | A Claude agent with tools — answers stock questions with live data from YFinance |
| `agno_agents/level_2_agent.py` | Agent with a knowledge base — LanceDB (hybrid vector search over the Agno docs), SQLite session storage and chat history |
| `agno_agents/level_3_agents.py` | Reasoning agent with persistent user memory (agentic memory), reasoning tools and YFinance tools |
| `agno_agents/level_4_agents_team.py` | A team of agents collaborating on a shared task |
| `agno_agents/level_5_workflow.py` | An agent workflow with response caching — repeat questions are answered from session state instantly |

## More Examples

- `agno_agents/agents_examples/reasearch_agent.py` — research agent using Exa and DuckDuckGo search
- `agno_agents/agents_examples/movie_agent.py` — movie recommendation agent

## Stack

Agno · OpenAI · Anthropic Claude · LanceDB · YFinance · Exa · DuckDuckGo Search · SQLAlchemy · Pydantic

## Getting Started

```bash
pip install -r requirements.txt
```

Create a `.env` file with your API keys (OpenAI and/or Anthropic), then run any level directly, e.g.:

```bash
python -m agno_agents.level_1_agent
```
