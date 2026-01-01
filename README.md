# Evolution of Todo - Phase I: In-Memory Python Console Application

This is a command-line todo manager built using spec-driven development with Claude Code. The application supports basic CRUD operations for tasks stored in memory only.

## Features

### Basic Features (Phase I)
1. **Add Task**: Create tasks with title and description
2. **View Tasks**: List all tasks with status indicators
3. **Update Task**: Modify existing task details
4. **Delete Task**: Remove tasks by unique ID
5. **Mark Complete/Incomplete**: Toggle task completion status

### Intermediate Features (Phase I - Enhanced)
6. **Due Dates**: Assign, update, and view tasks with due dates; see overdue indicators
7. **Priorities & Tags**: Set priority levels (High/Medium/Low) and categories (Work/Home/Personal)
8. **Search & Filter**: Find tasks by keyword or filter by status, priority, or tags
9. **Sort Tasks**: Organize task lists by due date, priority, title, or completion status

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies using UV:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

If you don't have UV installed:
```bash
pip install uv
```

## Usage

Run the application:
```bash
python src/main.py
```

The application will present a menu with options to:
- Add a new task
- View all tasks
- Update an existing task
- Delete a task
- Mark a task as complete/incomplete
- Exit the application

## Project Structure

```
/
├── sp.constitution (project principles)
├── /specs_history (all specification files)
├── /src (Python source code)
├── README.md (this file)
└── CLAUDE.md (Claude Code interaction guidelines)
```

## Development Process

This project was built using spec-driven development with Claude Code. All code was generated from specifications in the `/specs_history` folder, with no manual coding allowed. The process followed these steps:

1. Write specification in markdown
2. Submit to Claude Code via Spec-Kit Plus workflow
3. Review generated code against acceptance criteria
4. Refine spec if output is incorrect (no manual code fixes allowed)
5. Iterate until Claude Code generates correct implementation

## Technology Stack

- Python 3.13+
- UV package manager
- Claude Code for AI-assisted code generation
- Spec-Kit Plus for workflow management

## Phase I Scope

This is an in-memory, console-based application. No database, no API, no cloud deployment, no AI chatbot integration. Focus on mastering the spec-driven development workflow with Claude Code.