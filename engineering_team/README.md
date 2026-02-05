# Engineering Team (CrewAI Powered)

---

## English

A fully automated software development team based on [CrewAI](https://crewai.com).
Given a text-based requirement, this AI team automatically performs system design, writes backend code, builds a frontend interface (Gradio), and generates unit tests.

### Project Features

This project simulates a real software development team, composed of four AI Agents:

1.  **Engineering Lead**: Analyzes requirements and produces a detailed Markdown design document.
2.  **Backend Engineer**: Writes Python core logic modules based on the design document.
3.  **Frontend Engineer**: Creates a Gradio web interface (`app.py`) for the backend module.
4.  **Test Engineer**: Writes and executes unit tests for the backend code.

### Installation Requirements

*   Python >=3.10, <3.13
*   [uv](https://github.com/astral-sh/uv)
*   **Docker Desktop** (CrewAI requires Docker for sandbox isolation when AI executes code)

### Quick Start

#### 1. Set up Environment Variables

Create a `.env` file in the project root directory and fill in your API Keys:

```bash
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
```

#### 2. Install Dependencies

This project uses `uv` for management. Please ensure to install in editable mode (`-e`) to ensure the system correctly recognizes the project module name.

```bash
uv sync
uv pip install -e .
```

#### 3. Run the Project

Execute the main development workflow:

```bash
uv run engineering_team
# Or
python src/engineering_team/main.py
```

After execution, the AI team will start working, and the final output files will be stored in the `output/` folder:
*   `output/xxx_design.md` (Design document)
*   `output/xxx.py` (Backend code)
*   `output/app.py` (Frontend interface)
*   `output/test_xxx.py` (Test code)

### Frequently Asked Questions (Troubleshooting)

#### Q1: Encountering `RuntimeError: Docker is not running`
**Reason**: The Backend Engineer and Test Engineer have enabled code execution (`allow_code_execution=True`), and CrewAI strictly requires Docker for safety.
**Solution**:
1.  Please download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2.  Start Docker and wait for its status to show "Running".
3.  Re-run the program.

#### Q2: Encountering `ModuleNotFoundError: No module named 'engineering_team'`
**Reason**: The Python environment has not yet registered your project folder as an importable module, often occurring during project renaming or initial setup.
**Solution**: Please ensure you have performed the editable mode installation command:
```bash
uv pip install -e .
uv run engineering_team
```

### Project Structure

```
engineering_team/
├── output/
│   └── accounts.py_design.md
├── pyproject.toml
├── README.md
├── src/
│   └── engineering_team/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       ├── __init__.py
│       ├── main.py
│       └── tools/
│           ├── custom_tool.py
│           └── __init__.py
└── uv.lock
```

*   `src/engineering_team/config/`：Configuration files for agents (`agents.yaml`) and tasks (`tasks.yaml`).
*   `src/engineering_team/crew.py`：Main CrewAI logic, defining the assembly of Crew, Agents, and Tasks.
*   `src/engineering_team/main.py`：Program entry point, setting input parameters (Requirements).
*   `output/`：Stores all AI-generated code and documents.

---

## 中文說明 (Traditional Chinese)

基於 [CrewAI](https://crewai.com) 的全自動軟體開發團隊。
只要給它一段文字需求，這個 AI 團隊就會自動進行系統設計、編寫後端程式碼、建立前端介面 (Gradio)，並撰寫單元測試。

### 專案功能

本專案模擬一個真實的軟體開發小組，由四位 AI Agents 組成：

1.  **技術主管 (Engineering Lead)**：分析需求，產出詳細的 Markdown 設計文件。
2.  **後端工程師 (Backend Engineer)**：根據設計文件，撰寫 Python 核心邏輯模組。
3.  **前端工程師 (Frontend Engineer)**：為後端模組製作一個 Gradio 網頁介面 (`app.py`)。
4.  **測試工程師 (Test Engineer)**：針對後端程式碼撰寫並執行單元測試。

### 安裝需求

*   Python >=3.10, <3.13
*   [uv](https://github.com/astral-sh/uv)
*   **Docker Desktop** (因為 AI 會執行程式碼，CrewAI 預設需要 Docker 進行 sandbox 隔離)

### 快速開始

#### 1. 設定環境變數

在專案根目錄建立一個 `.env` 檔案，填入 API Key：

```bash
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
```

#### 2. 安裝依賴

本專案使用 `uv` 進行管理。請務必使用 `-e` (Editable) 模式安裝，以確保系統能正確識別專案模組名稱。

```bash
uv sync
uv pip install -e .
```

#### 3. 執行專案

執行主要的開發流程：

```bash
uv run engineering_team
# 或
python src/engineering_team/main.py
```

執行後，AI 團隊將會開始工作，最終產出的檔案會存放在 `output/` 資料夾中：
*   `output/xxx_design.md` (設計圖)
*   `output/xxx.py` (後端程式)
*   `output/app.py` (前端介面)
*   `output/test_xxx.py` (測試程式)

### 常見問題 (Troubleshooting)

#### Q1: 出現 `RuntimeError: Docker is not running`
**原因**：Backend Engineer 和 Test Engineer 開啟了程式碼執行功能 (`allow_code_execution=True`)，CrewAI 為了安全強制要求使用 Docker。
**解法**：
1.  請下載並安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。
2.  啟動 Docker 並等待狀態顯示為 "Running"。
3.  重新執行程式即可。

#### Q2: 出現 `ModuleNotFoundError: No module named 'engineering_team'`
**原因**：Python 環境尚未將您的專案資料夾註冊為可引用的模組，通常發生在更名專案或初次設定時。
**解法**：請確保您已執行過開發模式安裝指令：
```bash
uv pip install -e .
uv run engineering_team
```

### 專案結構

```
engineering_team/
├── output/
│   └── accounts.py_design.md
├── pyproject.toml
├── README.md
├── src/
│   └── engineering_team/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       ├── __init__.py
│       ├── main.py
│       └── tools/
│           ├── custom_tool.py
│           └── __init__.py
└── uv.lock
```

*   `src/engineering_team/config/`：定義代理人 (`agents.yaml`) 與任務 (`tasks.yaml`) 的設定檔。
*   `src/engineering_team/crew.py`：CrewAI 的主要邏輯，定義 Crew、Agent 和 Task 的組裝方式。
*   `src/engineering_team/main.py`：程式入口點，設定輸入參數 (Requirements)。
*   `output/`：存放 AI 生成的所有程式碼與文件。