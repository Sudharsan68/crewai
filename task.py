from crewai import Task
from tools import scraper
from agent import web_search_agent


task_web = Task(
    description=(
        " Web search based on given quary in duckduckgo.come with top 3 listed sits. give the answer in 2 lines."
    ),
    expected_output=" always give the output in 2 line",
    tools=[scraper],
    agent=web_search_agent
)
