from crewai import Agent, Crew, Process, Task, TaskOutput
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Tuple, Any
from crewai_tools import SerperDevTool
import json

search_tool = SerperDevTool(n_results=3)

def validate_research_result(result: TaskOutput) -> Tuple[bool, Any]:
    try:
        result = result.raw
        #check word count
        word_count = len(result.split())
        if not result or word_count < 400:
            return (False, "Summary output is short (less than 400 words)")
        
        return (True, result.strip())

    except Exception as e:
        return (False, "Unexpected error during validation")

def validate_summary_result(result: TaskOutput) -> Tuple[bool, Any]:
    try:

        result = result.raw
        print("=========================================")
        print(result)
        print("=========================================")
        #Check word count
        word_count = len(result.split())
        if not result or word_count < 100:
            return (False, "Summary output is short (less than 100 words)")

        if word_count > 400:
            return (False, "Summary output is too long (more than 400 words)")
        # Check sentence count
        sentences = [s.strip().lower() for s in result.split('.') if len(s.strip()) > 10]
        if len(sentences) > 7:
            return (False, "Summary output should contain at most 7 meaningful sentences.")

        if not sentences or len(sentences) < 1:
            return (False, "Summary output should contain at least 1 meaningful sentences.")

        return (True, result.strip())
    except Exception as e:
        return (False, "Unexpected error during validation")

@CrewBase
class AnalystCrew():
    """AnalystCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )
    
    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )


    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            tools=[search_tool],
            guardrail=validate_research_result
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task'],
            guardrail=validate_summary_result
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AnalystCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
