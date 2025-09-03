from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import FileReadTool, DirectoryReadTool

@CrewBase
class CodeAnalyst():
    """CodeAnalyst crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config['coder'],
            tools=[
                DirectoryReadTool(directory='./src/code_analyst/assets/inputs_files'),
                FileReadTool()
            ],
            verbose=True,
        )
    
    @agent
    def executor(self) -> Agent:
        return Agent(
            config=self.agents_config['executor'],
            allow_code_execution=True,
            tools=[
                DirectoryReadTool(directory='./src/code_analyst/assets/inputs_files'),
                FileReadTool()
            ],
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def coder_task(self) -> Task:
        return Task(
            config=self.tasks_config['coder_task'],
            output_key='generated_code',
            output_file='./src/code_analyst/assets/outputs_files/script.py'
        )

    @task
    def executor_task(self) -> Task:
        def executor_handler(context):
            code = context.get("generated_code", "")
            if not code:
                return "No code was provided."
            try:
                exec_globals = {}
                exec(code, exec_globals)
                return exec_globals.get("result", "Code executed but no `result` variable found.")
            except Exception as e:
                return f"Execution error: {str(e)}"

        return Task(
            config=self.tasks_config['executor_task'],
            handler=executor_handler,
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='./src/code_analyst/assets/outputs_files/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CodeAnalyst crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
