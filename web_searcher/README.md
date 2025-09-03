# Web Searcher Crew

Welcome to the Web Searcher Crew project, powered by [crewAI](https://crewai.com). This project is designed to perform comprehensive research on any given topic using a multi-agent AI system. The crew consists of specialized agents that work together to research, summarize, and generate detailed reports about specified topics using web search capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` and `SERPER_API_KEY` into the `.env` file**

- Modify `src/web_searcher/config/agents.yaml` to define your agents
- Modify `src/web_searcher/config/tasks.yaml` to define your tasks
- Modify `src/web_searcher/crew.py` to add your own logic, tools and specific args
- Modify `src/web_searcher/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Web Searcher Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run research on "Egypt population growth" and create both a `summary.txt` file and a `report.md` file with the research findings.

## Understanding Your Crew

The Web Searcher Crew is composed of three specialized AI agents, each with unique roles and capabilities:

### 🔍 Researcher Agent
- **Role**: Senior Data Researcher specialized in the given topic
- **Goal**: Uncover cutting-edge developments and comprehensive information
- **Tools**: SerperDevTool for web searching with 3 results per query
- **Output**: Detailed research findings with statistics, trends, and recent developments

### 📝 Summarizer Agent  
- **Role**: Information Summarizer
- **Goal**: Create clear and concise summaries of research findings
- **Validation**: Ensures summaries are 100-400 words and contain 1-7 meaningful sentences
- **Output**: Structured summary saved to `summary.txt`

### 📊 Reporting Analyst Agent
- **Role**: Reporting Analyst  
- **Goal**: Create detailed reports based on data analysis and research findings
- **Input**: Uses summarized findings as context
- **Output**: Comprehensive markdown report saved to `report.md`

The crew follows a sequential process where each agent builds upon the previous agent's work, leveraging their collective skills to deliver comprehensive research reports on any specified topic.

```

## Configuration

### Environment Variables
Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### Customizing Research Topics
Edit the `inputs` dictionary in `src/web_searcher/main.py` to change the research topic:
```python
inputs = {
    'topic': 'Your desired research topic',
    'current_year': str(datetime.now().year)
}
```
