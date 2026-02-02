# Deep Research Multi-Agent System

An automated, AI-powered research assistant built with **Python**, **OpenAI**, and **Gradio**. 

This system orchestrates a team of specialized AI agents to plan research strategies, perform parallel web searches, synthesize findings into a comprehensive report, and email the final result to the user.

## Features

*   **Multi-Agent Architecture**: distinct agents for Planning, Searching, Writing, and Emailing.
*   **Parallel Execution**: Uses Python's `asyncio` to perform multiple web searches simultaneously, significantly reducing wait times.
*   **Structured Outputs**: Leverages **Pydantic** to ensure strict data schemas between agents (no more broken JSON!).
*   **Real-time UI**: A **Gradio** web interface that streams the research progress and final report.
*   **Automated Reporting**: Generates a Markdown report and sends a formatted HTML email via **SendGrid**.

## System Architecture

The system is controlled by a **Research Manager** that coordinates the following workflow:

1.  **Planner Agent**: Analyzes the user's query and generates a list of 3 specific web search terms.
2.  **Search Agent**: Performs the searches in parallel (concurrently) to gather information efficiently.
3.  **Writer Agent**: Consumes the search results, creates an outline, and writes a detailed Markdown report with a summary and follow-up questions.
4.  **Email Agent**: Converts the report to HTML and sends it to the configured recipient.

## Prerequisites

*   Python 3.10+
*   OpenAI API Key
*   SendGrid API Key (for email functionality)

## Installation

1.  **Navigate to the project directory**:
    If you have cloned the entire `SomeAgents` repository, please enter the `deep_research` directory:
    ```bash
    cd deep_research
    ```

2.  **Create and activate virtual environment**:
    ```bash
    uv venv
    source .venv/bin/activate  # macOS/Linux
    # .venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies**:
    Install all dependencies from `requirements.txt` using `uv`:
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```ini
    OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
    SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxx
    ```

## Configuration

**Important:** Before running, you must configure the email sender and recipient in `email_agent.py`.

Open `email_agent.py` and modify the following lines:

```python
from_email = Email("your-verified-sender@example.com")  # Must be verified in SendGrid
to_email = To("your-email@example.com")      # Where you want to receive reports
```

## Usage
``` bash
python deep_research.py
```

Once running, a local URL will appear in your terminal (e.g., http://127.0.0.1:7860). Open this link in your browser to access the Deep Research interface.

1. Enter a research topic (e.g., "The future of solid-state batteries").
2. Click Run.
3. Watch the agents plan, search, and write in real-time!

## Project Structure
- `deep_research.py`: The entry point. Sets up the Gradio UI and triggers the manager.
- `research_manager.py`: The orchestrator. Manages the lifecycle of the research process and data flow between agents.
- `planner_agent.py`: Agent responsible for breaking down the query into search terms.
- `search_agent.py`: Agent responsible for executing web searches and summarizing results.
- `writer_agent.py`: Agent responsible for synthesizing information into a final report.
- `email_agent.py`: Agent responsible for formatting and sending the email.
g