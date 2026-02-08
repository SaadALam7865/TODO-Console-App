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
6. **Search Tasks**: Find tasks by keyword in title or description
7. **Filter Tasks**: Show tasks by criteria (status, priority, tags, due date status)
8. **Sort Tasks**: Organize task lists by various criteria (due date, priority, title, creation order, completion status)
9. **Due Dates**: Assign, update, and view tasks with due dates; see overdue indicators
10. **Priorities & Tags**: Set priority levels (High/Medium/Low) and categories (Work/Home/Personal)

### Advanced Features (Phase I - Intelligent)
11. **Recurring Tasks**: Create tasks that automatically repeat on daily/weekly/monthly schedules after completion
12. **Time Reminders & Notifications**: Set specific times for browser notifications before due dates
13. **Upcoming Reminders**: View tasks with upcoming notifications

### Complete Feature List
The application now includes all 11 core features (5 basic + 5 intermediate + 2 advanced) plus the Exit option:

1. Add Task: Create task with title, description, due date, priority, tags, recurrence, and reminders
2. View Tasks: List all tasks with status indicators
3. Update Task: Modify existing task details
4. Delete Task: Remove task by unique ID
5. Mark Complete/Incomplete: Toggle task completion status
6. Search Tasks: Find tasks by keyword in title or description
7. Filter Tasks: Show tasks by criteria (status, priority, tags, due date status)
8. Sort Tasks: Order tasks by various criteria (due date, priority, title, creation order, completion status)
9. Set/View Recurring Pattern: Configure recurring tasks with daily/weekly/monthly intervals
10. Set/View Reminder: Configure task reminders with specific timing before due dates
11. View Upcoming Reminders: See tasks with upcoming notifications
12. Exit: Close the application

### Advanced Feature Usage Examples

#### Recurring Tasks
- Create a recurring task when adding a task by specifying recurrence pattern (daily/weekly/monthly)
- Set recurrence interval (e.g., every 2 days, every 1 week)
- Optionally set an end date for the recurrence
- When a recurring task is marked as complete, a new instance is automatically created based on the recurrence pattern

#### Time Reminders & Notifications
- Set a reminder time in minutes before the due date (e.g., 30 minutes before)
- The scheduler service runs in the background and checks for upcoming reminders
- When a reminder is due, a notification is triggered
- Use the "View Upcoming Reminders" option to see tasks with pending notifications

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

## Phase I Completion Status

Phase I: In-Memory Python Console Application is now complete with all 11 features implemented:
- 5 Basic features: Add, View, Update, Delete, Toggle status
- 5 Intermediate features: Search, Filter, Sort, Due dates, Priorities & Tags
- 2 Advanced features: Recurring tasks, Time reminders & notifications

The application includes all functionality with a complete CLI menu system and is ready for use.

## Technology Stack

- Python 3.13+
- UV package manager
- Claude Code for AI-assisted code generation
- Spec-Kit Plus for workflow management

## Phase I Scope

This is an in-memory, console-based application. No database, no API, no cloud deployment, no AI chatbot integration. Focus on mastering the spec-driven development workflow with Claude Code.