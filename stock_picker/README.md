# Stock Picker Crew

---

## English

A CrewAI-powered team of agents designed to analyze stock sectors and provide investment insights. This project uses the powerful and flexible framework provided by [crewAI](https://crewai.com) to enable AI agents to collaborate effectively on financial analysis tasks.

### Installation

Ensure you have Python >=3.10, <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

1.  **Install UV** (if you haven't already):
    ```bash
    pip install uv
    ```

2.  **Navigate to your project directory** and create a virtual environment:
    ```bash
    uv venv
    source .venv/bin/activate # macOS/Linux
    # .venv\Scripts\activate  # Windows
    ```

3.  **Install Dependencies**:
    This project is managed by `uv`. Ensure you install in editable mode (`-e`) so that the system can correctly recognize the project's runnable scripts.
    ```bash
    uv sync
    uv pip install -e .
    ```

### Customizing

1.  **Set up API Keys**: Create a `.env` file in the project root and add your `OPENAI_API_KEY` and `SERPER_API_KEY`.
    ```
    OPENAI_API_KEY="sk-..."
    SERPER_API_KEY="..."
    ```

2.  **Define Agents & Tasks**:
    *   Modify `src/stock_picker/config/agents.yaml` to define your agents.
    *   Modify `src/stock_picker/config/tasks.yaml` to define your tasks.

3.  **Customize Inputs**:
    *   Modify `src/stock_picker/main.py` to change the default inputs (e.g., the `sector`) for your crew.

### Running the Project

You can run the project in several ways from your project's root folder:

1.  **Using the `uv` script (Recommended)**:
    This command uses the script defined in `pyproject.toml`.
    ```bash
    uv run stock_picker
    ```

2.  **Using `crewai`'s built-in CLI**:
    ```bash
    crewai run
    ```

3.  **Directly executing the main file**:
    ```bash
    python src/stock_picker/main.py
    ```

By default, the unmodified example will analyze the 'Technology' sector and print the final report directly to your console.

### Understanding Your Crew

The `stock_picker` Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

---

## 中文說明 (Traditional Chinese)

一個由 CrewAI 驅動的 AI 代理團隊，旨在分析股票領域並提供投資見解。本專案使用功能強大且靈活的 [crewAI](https://crewai.com) 框架，使 AI 代理能夠在金融分析任務上進行有效協作。

### 安裝

請確保您的系統已安裝 Python >=3.10, <3.13。本專案使用 [UV](https://docs.astral.sh/uv/) 進行依賴管理。

1.  **安裝 UV** (若尚未安裝):
    ```bash
    pip install uv
    ```

2.  **進入專案目錄**並建立虛擬環境:
    ```bash
    uv venv
    source .venv/bin/activate # macOS/Linux
    # .venv\Scripts\activate  # Windows
    ```

3.  **安裝依賴**:
    本專案使用 `uv` 管理。請務必使用可編輯模式 (`-e`) 安裝，以確保系統能正確識別專案的可執行腳本。
    ```bash
    uv sync
    uv pip install -e .
    ```

### 客製化

1.  **設定 API 金鑰**: 在專案根目錄建立一個 `.env` 檔案，並加入您的 `OPENAI_API_KEY`。
    ```
    OPENAI_API_KEY="sk-..."
    ```

2.  **定義代理與任務**:
    *   修改 `src/stock_picker/config/agents.yaml` 來定義您的代理。
    *   修改 `src/stock_picker/config/tasks.yaml` 來定義您的任務。

3.  **客製化輸入**:
    *   修改 `src/stock_picker/main.py` 來更改您團隊的預設輸入（例如 `sector`）。

### 執行專案

您可以從專案的根目錄透過以下幾種方式執行專案：

1.  **使用 `uv` 腳本 (建議)**:
    此指令會使用 `pyproject.toml` 中定義的腳本。
    ```bash
    uv run stock_picker
    ```

2.  **使用 `crewai` 的內建 CLI**:
    ```bash
    crewai run
    ```

3.  **直接執行主檔案**:
    ```bash
    python src/stock_picker/main.py
    ```

在預設情況下，未經修改的範例將會分析「科技」領域，並將最終報告直接印在終端機上。

### 了解您的團隊

`stock_picker` 團隊由多個 AI 代理組成，每個代理都有獨特的角色、目標和工具。這些代理在一系列於 `config/tasks.yaml` 中定義的任務上協作，利用他們的集體技能來達成複雜的目標。`config/agents.yaml` 檔案則概述了您團隊中每個代理的能力和設定。