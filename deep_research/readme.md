# Deep Research Multi-Agent System

An automated, AI-powered research assistant built with Python, OpenAI, and Gradio.


This system orchestrates a team of specialized AI agents to plan research strategies, perform parallel web searches, synthesize findings into a comprehensive report, and email the final result to the user.

## Features

*   **Multi-Agent Architecture**: distinct agents for Planning, Searching, Writing, and Emailing.
*   **Parallel Execution**: Uses Python's `asyncio` to perform multiple web searches simultaneously, significantly reducing wait times.
*   **Structured Outputs**: Leverages **Pydantic** to ensure strict data schemas between agents.
*   **Real-time UI**: A **Gradio** web interface that streams the research progress and final report.
*   **Automated Reporting**: Generates a Markdown report and sends a formatted HTML email via **SendGrid**.



## Prerequisites

*   Python >= 3.11
*   [uv](https://github.com/astral-sh/uv) installed
*   OpenAI API Key
*   SendGrid API Key (for email functionality)

## Installation

1.  **Navigate to the project directory**:
    ```bash
    cd deep_research
    ```

2.  **Install dependencies**:
    This command syncs your environment with the dependencies listed in `pyproject.toml`.

    ```bash
    uv sync
    ```

3.  **Set up Environment Variables**:
    Create a `.env` file and add your API keys:
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
uv run main.py
```

Open the local URL provided in your terminal (e.g., http://127.0.0.1:7860) in your browser.
