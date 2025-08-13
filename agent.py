import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import scraper

# Load env
load_dotenv()
api_key = os.environ.get("OPEN_ROUTER")

# LLM
llm = LLM(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

web_search_agent = Agent(
    role="Web Search Agent",
    tools=[scraper],
    goal=("Find most accurate to users query"),
    backstory=("user search for the best answer"),
    verbose=True,
    allow_delegation=True,
    llm=llm
)


