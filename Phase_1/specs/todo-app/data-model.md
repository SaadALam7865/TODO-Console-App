# Data Model: Todo In-Memory Python Console Application

## Task Entity

### Fields
- `id`: int (required, unique, auto-generated)
  - Sequential integer starting from 1
  - Primary identifier for the task
  - Used for all operations (update, delete, toggle)
- `title`: str (required, non-empty)
  - Task title/description in brief
  - Must be non-empty string
  - Max length: No specific limit (limited by console display)
- `description`: str (optional)
  - Detailed description of the task
  - Can be empty string if not provided
  - Max length: No specific limit
- `completed`: bool (required, default: False)
  - Status indicator for task completion
  - False = incomplete, True = complete
  - Toggled by mark complete/incomplete feature

### Validation Rules
- `id`: Must be positive integer, unique across all tasks
- `title`: Must be non-empty after stripping whitespace
- `description`: Optional, but if provided must be string
- `completed`: Boolean value only (True/False)

### State Transitions
- `completed` field toggles between False and True states
- Initial state: `completed = False`
- Transition trigger: Mark Complete/Incomplete feature
- No other state transitions in this model

## Task Collection

### Storage Structure
- `tasks`: dict[int, Task]
  - Dictionary mapping task ID to Task object
  - Provides O(1) lookup by ID
  - Maintains all tasks in memory during application session
- `next_id`: int
  - Tracks the next available ID for new tasks
  - Incremented after each task creation
  - Ensures unique ID generation

### Operations
- **Create**: Add new Task object to tasks dictionary with new ID
- **Read**: Retrieve Task object by ID from tasks dictionary
- **Update**: Modify Task object fields in-place in dictionary
- **Delete**: Remove Task object from tasks dictionary by ID
- **List**: Return all Task objects from tasks dictionary sorted by ID

## Relationships
- No relationships between Task entities
- All tasks are independent
- Single collection (tasks dictionary) holds all task instances