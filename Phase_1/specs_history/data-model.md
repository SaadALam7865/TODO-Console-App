# Data Model: Enhanced Task Structure for Phase I Advanced Features - Intelligent Automation

## Entity: Task (Fully Enhanced)

### Core Fields (Inherited from Basic Features)
| Field | Type | Required | Default | Validation | Description |
|-------|------|----------|---------|------------|-------------|
| id | int | Yes | N/A | Positive integer, unique | Unique identifier for the task |
| title | str | Yes | N/A | Non-empty string | Title/description of the task |
| description | str | No | "" | String (can be empty) | Detailed description of the task |
| complete | bool | Yes | False | Boolean value | Completion status of the task |

### Intermediate Fields (Inherited from Due Dates, Priorities, Tags)
| Field | Type | Required | Default | Validation | Description |
|-------|------|----------|---------|------------|-------------|
| due_date | str or None | No | None | YYYY-MM-DD or YYYY-MM-DD HH:MM format, valid date | Optional due date in ISO format with time support |
| priority | str | Yes | "Medium" | One of: "High", "Medium", "Low" (case-insensitive) | Priority level of the task |
| tags | list | Yes | [] | List of valid tag strings | Categories assigned to the task |
| created_at | str | Yes | Current timestamp | ISO 8601 format | Timestamp when task was created |

### Advanced Fields (New for Recurring Tasks & Time Reminders)
| Field | Type | Required | Default | Validation | Description |
|-------|------|----------|---------|------------|-------------|
| recurrence_pattern | str or None | No | None | One of: "daily", "weekly", "monthly", None | Recurrence pattern for automatic task generation |
| recurrence_interval | int | No | 1 | Positive integer (≥ 1) | Interval multiplier for recurrence (e.g., every 2 weeks) |
| recurrence_end_date | str or None | No | None | YYYY-MM-DD format, after current due_date if set | End date for recurrence (optional) |
| reminder_time | int or None | No | None | Positive integer representing minutes before due date | Minutes before due date to send notification |
| last_notification_sent | str or None | No | None | ISO 8601 timestamp format when set | Timestamp of last notification sent |
| is_recurring_instance | bool | No | False | Boolean value | Flag to identify if this is a generated recurring instance |
| parent_task_id | int or None | No | None | Positive integer if set | Reference to parent task for recurring instances |

### Valid Tag Values
- "Work"
- "Home"
- "Personal"

### Valid Recurrence Patterns
- "daily" - Repeat every N days
- "weekly" - Repeat every N weeks
- "monthly" - Repeat every N months
- None - No recurrence (default)

### Priority Order
- High > Medium > Low (for sorting purposes)

### Relationships
- **parent_task_id** → references **id** of original recurring task (for recurring instances)

### State Transitions
- complete: False ↔ True (toggle via mark complete/incomplete feature)
- due_date: Can be added, modified, or removed (now supports time component)
- priority: Can be changed between High/Medium/Low
- tags: Can be added or removed from the list
- recurrence_pattern: Can be set to enable/disable recurrence
- reminder_time: Can be set to enable/disable notifications

## Validation Rules

### Due Date Validation
- Format must be YYYY-MM-DD or YYYY-MM-DD HH:MM (ISO 8601)
- Must represent a valid calendar date/time (e.g., not February 30th)
- Can be None (optional field)
- When present, used for overdue calculations and reminder scheduling

### Priority Validation
- Must be one of: "High", "Medium", "Low"
- Case-insensitive input accepted
- Internally stored as capitalized form ("High", "Medium", "Low")
- Default value: "Medium" if not specified

### Tag Validation
- Each tag must be one of: "Work", "Home", "Personal"
- Case-insensitive input accepted
- Internally stored as capitalized form
- Multiple tags allowed (list)
- Duplicate tags should be prevented
- Default value: empty list [] if not specified

### Recurrence Validation
- recurrence_pattern must be one of: "daily", "weekly", "monthly", None
- recurrence_interval must be a positive integer (≥ 1)
- if recurrence_end_date is set, it must be after the current due_date in YYYY-MM-DD format
- recurrence_end_date must be in YYYY-MM-DD format if set

### Reminder Validation
- reminder_time, if set, must be a positive integer representing minutes before due date
- last_notification_sent must be in ISO timestamp format when set

### Overdue Logic
- A task is considered overdue if:
  - due_date is not None
  - due_date (date part only) is before the current date
- Overdue status is computed dynamically based on current date

### Recurring Task Logic
- When a task with recurrence_pattern is marked complete:
  - A new task instance is created with updated due_date based on recurrence pattern
  - New task inherits all properties from parent except due_date and completion status
  - is_recurring_instance is set to True for the new task
  - parent_task_id references the original task ID

## Backward Compatibility

### Handling Existing Tasks
- Tasks created without new fields will have:
  - due_date = None (unchanged)
  - priority = "Medium" (unchanged)
  - tags = [] (unchanged)
  - created_at = timestamp (unchanged)
  - recurrence_pattern = None (new field, default)
  - recurrence_interval = 1 (new field, default)
  - recurrence_end_date = None (new field, default)
  - reminder_time = None (new field, default)
  - last_notification_sent = None (new field, default)
  - is_recurring_instance = False (new field, default)
  - parent_task_id = None (new field, default)

### Migration Strategy
- No database migration needed (in-memory storage)
- Default values ensure existing functionality continues to work
- Display formatting handles None values gracefully
- All 9 existing features continue to work unchanged

## Example Instances

### New Task with All Advanced Features
```python
{
  "id": 1,
  "title": "Weekly team meeting",
  "description": "Attend the weekly team sync meeting",
  "complete": False,
  "due_date": "2026-01-08 10:00",
  "priority": "Medium",
  "tags": ["Work"],
  "created_at": "2026-01-01T10:30:00",
  "recurrence_pattern": "weekly",
  "recurrence_interval": 1,
  "recurrence_end_date": "2026-12-31",
  "reminder_time": 60,
  "last_notification_sent": None,
  "is_recurring_instance": False,
  "parent_task_id": None
}
```

### Recurring Task Instance (Generated)
```python
{
  "id": 2,
  "title": "Weekly team meeting",
  "description": "Attend the weekly team sync meeting",
  "complete": False,
  "due_date": "2026-01-15 10:00",
  "priority": "Medium",
  "tags": ["Work"],
  "created_at": "2026-01-08T11:00:00",
  "recurrence_pattern": "weekly",
  "recurrence_interval": 1,
  "recurrence_end_date": "2026-12-31",
  "reminder_time": 60,
  "last_notification_sent": None,
  "is_recurring_instance": True,
  "parent_task_id": 1
}
```

### Task with Time-based Reminder Only
```python
{
  "id": 3,
  "title": "Doctor appointment",
  "description": "Annual health checkup",
  "complete": False,
  "due_date": "2026-01-15 14:30",
  "priority": "High",
  "tags": ["Personal"],
  "created_at": "2026-01-01T10:35:00",
  "recurrence_pattern": None,
  "recurrence_interval": 1,
  "recurrence_end_date": None,
  "reminder_time": 120,  # 2 hours before
  "last_notification_sent": "2026-01-15T12:30:00",
  "is_recurring_instance": False,
  "parent_task_id": None
}
```

### Minimal Task (Backward Compatible)
```python
{
  "id": 4,
  "title": "Buy groceries",
  "description": "",
  "complete": False,
  "due_date": None,
  "priority": "Medium",
  "tags": [],
  "created_at": "2026-01-01T10:40:00",
  "recurrence_pattern": None,
  "recurrence_interval": 1,
  "recurrence_end_date": None,
  "reminder_time": None,
  "last_notification_sent": None,
  "is_recurring_instance": False,
  "parent_task_id": None
}
```

## API Contract Implications

### Task Creation
- All new fields are optional in creation (will use defaults)
- Validation must occur before saving
- created_at is automatically set to current timestamp
- Advanced fields can be set during creation to enable features immediately

### Task Updates
- Individual fields can be updated independently
- Validation must occur for each updated field
- Other fields remain unchanged
- Recurrence and reminder settings can be modified after creation

### Task Retrieval
- All fields returned in response
- None values for optional fields are preserved
- Default values are returned for missing fields in old tasks
- Advanced features are exposed through the same interface

### Task Completion
- When recurring tasks are marked complete, new instances are automatically created
- New instances inherit all properties from parent task
- System handles recurrence logic automatically