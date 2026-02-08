# Todo Application API Contracts

## Task Management API

### Core Operations

#### Add Task
- **Method**: `TodoApp.add_task(title: str, description: str) -> Task`
- **Input**:
  - `title`: Non-empty string (required)
  - `description`: String (optional)
- **Output**: Task object with generated ID
- **Success**: Returns new Task object with unique ID
- **Error**: Raises ValueError if title is empty

#### View Tasks
- **Method**: `TodoApp.view_tasks() -> List[Task]`
- **Input**: None
- **Output**: List of all Task objects, sorted by ID
- **Success**: Returns list of all tasks
- **Error**: None (returns empty list if no tasks)

#### Update Task
- **Method**: `TodoApp.update_task(task_id: int, title: Optional[str], description: Optional[str]) -> Task`
- **Input**:
  - `task_id`: Valid task ID
  - `title`: New title (optional, None means no change)
  - `description`: New description (optional, None means no change)
- **Output**: Updated Task object
- **Success**: Returns updated Task object
- **Error**: Raises ValueError if task_id doesn't exist or title is empty

#### Delete Task
- **Method**: `TodoApp.delete_task(task_id: int) -> Task`
- **Input**: `task_id`: Valid task ID
- **Output**: Deleted Task object
- **Success**: Returns deleted Task object, removes from storage
- **Error**: Raises ValueError if task_id doesn't exist

#### Toggle Task Status
- **Method**: `TodoApp.toggle_task_status(task_id: int) -> Task`
- **Input**: `task_id`: Valid task ID
- **Output**: Task object with toggled completion status
- **Success**: Returns Task with completion status flipped
- **Error**: Raises ValueError if task_id doesn't exist

## Data Contracts

### Task Object
```python
class Task:
    id: int          # Unique identifier (positive integer)
    title: str       # Task title (non-empty after stripping)
    description: str # Task description (can be empty)
    completed: bool  # Completion status (True/False)
```

### Error Contracts
- **ValueError**: Thrown for invalid inputs (missing title, invalid ID)
- **TypeError**: Thrown for incorrect parameter types