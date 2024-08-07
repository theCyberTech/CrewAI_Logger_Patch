# run_crew.py
import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import OpenAI

def run_crew():
    # Use environment variable for API key
    openai_api_key = os.environ['OPENAI_API_KEY']

    researcher = Agent(
        role='Researcher',
        goal='Provide a brief summary on a given topic',
        backstory='You are a knowledgeable researcher with expertise in various fields.',
        verbose=True,
        allow_delegation=False,
        llm=OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    )

    research_task = Task(
        description='Provide a brief summary about the gievn topic.',
        expected_output='A concise paragraph summarizing key points about the given topic.',
        agent=researcher
    )

    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=2,
        process=Process.sequential
    )

    result = crew.kickoff()
    
    # Write result to a file
    with open('ai_summary.md', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    run_crew()
