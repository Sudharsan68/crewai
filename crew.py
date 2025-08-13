from crewai import Crew, Process
from agent import web_search_agent
from task import task_web



# Crew
crew = Crew(
    agents=[web_search_agent],
    tasks=[task_web],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"question": "give me 2 line of code to print hello world in python"})
print(result)