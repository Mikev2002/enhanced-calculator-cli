# Enhanced-Calculator-cli


A command-line calculator application with advanced arithmetic, history tracking, undo/redo functionality, logging, auto-save, and CI/CD pipeline.

---

## 📦 Features

-  Basic Operations: add, subtract, multiply, divide
-  Advanced Operations: power, root, modulus, integer division, percentage, absolute difference
-  Undo/Redo support (Memento Design Pattern)
-  History tracking
-  Configurable settings via `.env` (using `python-dotenv`)
-  Logging to file (Observer Pattern)
-  Auto-save calculation history to CSV using `pandas`
-  REPL Command-line Interface
-  CI/CD with GitHub Actions
-  90%+ unit test coverage via `pytest` and `pytest-cov`

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Mikev2002/enhanced-calculator-cli.git
cd enhanced-calculator-cli


2. Create and Activate Virtual Environment

py -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux

3. Install Dependencies

pip install -r requirements.txt


4. Configuration

Create a .env file in the project root:
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8

Usage (REPL):
python main.py

Available Commands:
add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
undo        - Undo last calculation
redo        - Redo undone calculation
history     - Show history
clear       - Clear all history
help        - Show command help
exit        - Exit the program


 Running Tests With Coverage: 
 pytest
pytest --cov=app


🚀 CI/CD (GitHub Actions)

CI runs on every push or pull request to main and will:

Install dependencies

Run tests

Fail if coverage < 90%

Workflow file: .github/workflows/python-app.yml




🧠 Design Patterns Used

Factory – Dynamic operation creation

Memento – Undo/Redo calculation history

Observer – Logging & auto-save with event-based updates


Author

Mike Villagomez
Midterm Project-Enhanced-Calculator-cli