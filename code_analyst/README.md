# Code Analyst Crew

Welcome to the Code Analyst Crew project, powered by [crewAI](https://crewai.com). This project is designed to analyze data through automated code generation and execution using a multi-agent AI system. The crew consists of specialized agents that work together to write Python code, execute it safely, and generate comprehensive reports based on data analysis queries.

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

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/code_analyst/config/agents.yaml` to define your agents
- Modify `src/code_analyst/config/tasks.yaml` to define your tasks
- Modify `src/code_analyst/crew.py` to add your own logic, tools and specific args
- Modify `src/code_analyst/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Code Analyst Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will analyze the "Bank Customer Churn Prediction.csv" dataset to answer "What is the churn rate in France country?" and create both a Python script (`script.py`) and a comprehensive report (`report.md`) in the `assets/outputs_files/` directory.

## Understanding Your Crew

The Code Analyst Crew is composed of three specialized AI agents, each with unique roles and capabilities:

### 🧑‍💻 Coder Agent
- **Role**: Python Coder specialized in data analysis
- **Goal**: Write and optimize Python code to answer data queries
- **Tools**: FileReadTool and DirectoryReadTool for accessing input files
- **Safety**: Ensures code is safe without dangerous operations (file deletion, subprocess calls, OS commands)
- **Output**: Well-structured Python code saved to `assets/outputs_files/script.py`

### ⚡ Executor Agent  
- **Role**: Code Executor
- **Goal**: Execute and validate Python code snippets safely
- **Capabilities**: Allow code execution with built-in error handling
- **Tools**: File access tools for reading input data
- **Validation**: Catches errors and ensures code runs correctly, expects results in a `result` variable

### 📊 Reporting Analyst Agent
- **Role**: Reporting Analyst  
- **Goal**: Create detailed reports based on query results and code analysis
- **Input**: Uses code execution results and analysis findings
- **Output**: Comprehensive report saved to `assets/outputs_files/report.md`

The crew follows a sequential process: **Code Generation → Code Execution → Report Generation**, ensuring reliable data analysis with comprehensive documentation.

## Project Structure

```
code_analyst/
├── src/code_analyst/
│   ├── assets/
│   │   ├── inputs_files/          # Place your CSV/data files here
│   │   │   └── Bank Customer Churn Prediction.csv
│   │   └── outputs_files/         # Generated scripts and reports
│   │       ├── script.py          # Generated Python code
│   │       └── report.md          # Analysis report
│   ├── config/
│   │   ├── agents.yaml           # Agent configurations
│   │   └── tasks.yaml            # Task definitions
│   ├── crew.py                   # Main crew logic
│   └── main.py                   # Entry point and configurations
```

## Configuration

### Environment Variables
Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Customizing Analysis Queries
Edit the `inputs` dictionary in `src/code_analyst/main.py` to change the analysis query:
```python
inputs = {
    'topic': 'Your data analysis question here',
}
```

### Adding Data Files
1. Place your CSV or data files in `src/code_analyst/assets/inputs_files/`
2. The agents will automatically access files from this directory
3. Update your query in `main.py` to reference your specific data and analysis needs

## Example Queries
- "What is the average age of customers by region?"
- "Calculate the correlation between income and purchase amount"
- "Find the top 10 products by sales volume"
- "What is the churn rate in France country?" (default example)
