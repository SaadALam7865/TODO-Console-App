# Data Model: Enhanced Task Structure for Phase I Intermediate Features

## Entity: Task (Enhanced)

### Fields

| Field | Type | Required | Default | Validation | Description |
|-------|------|----------|---------|------------|-------------|
| id | int | Yes | N/A | Positive integer, unique | Unique identifier for the task |
| title | str | Yes | N/A | Non-empty string | Title/description of the task |
| description | str | No | "" | String (can be empty) | Detailed description of the task |
| complete | bool | Yes | False | Boolean value | Completion status of the task |
| due_date | str or None | No | None | YYYY-MM-DD format, valid date | Optional due date in ISO format |
| priority | str | Yes | "Medium" | One of: "High", "Medium", "Low" (case-insensitive) | Priority level of the task |
| tags | list | Yes | [] | List of valid tag strings | Categories assigned to the task |
| created_at | str | Yes | Current timestamp | ISO 8601 format | Timestamp when task was created |

### Valid Tag Values
- "Work"
- "Home"
- "Personal"

### Priority Order
- High > Medium > Low (for sorting purposes)

### Relationships
- None (standalone entity)

### State Transitions
- complete: False ↔ True (toggle via mark complete/incomplete feature)
- due_date: Can be added, modified, or removed
- priority: Can be changed between High/Medium/Low
- tags: Can be added or removed from the list

## Validation Rules

### Due Date Validation
- Format must be YYYY-MM-DD (ISO 8601)
- Must represent a valid calendar date (e.g., not February 30th)
- Can be None (optional field)
- When present, used for overdue calculations

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

### Overdue Logic
- A task is considered overdue if:
  - due_date is not None
  - due_date is before the current date (comparison based on YYYY-MM-DD format)
- Overdue status is computed dynamically based on current date

## Backward Compatibility

### Handling Existing Tasks
- Tasks created without new fields will have:
  - due_date = None
  - priority = "Medium"
  - tags = []
  - created_at = timestamp of when field was added (or migration timestamp)

### Migration Strategy
- No database migration needed (in-memory storage)
- Default values ensure existing functionality continues to work
- Display formatting handles None values gracefully

## Example Instances

### New Task with All Fields
```python
{
  "id": 1,
  "title": "Complete project proposal",
  "description": "Finish and submit the project proposal to stakeholders",
  "complete": False,
  "due_date": "2026-01-15",
  "priority": "High",
  "tags": ["Work", "Urgent"],
  "created_at": "2026-01-01T10:30:00"
}
```

### Minimal Task (Backward Compatible)
```python
{
  "id": 2,
  "title": "Buy groceries",
  "description": "",
  "complete": False,
  "due_date": None,
  "priority": "Medium",
  "tags": [],
  "created_at": "2026-01-01T10:35:00"
}
```

### Completed Task with Due Date
```python
{
  "id": 3,
  "title": "Team meeting",
  "description": "Weekly team sync meeting",
  "complete": True,
  "due_date": "2025-12-30",
  "priority": "Medium",
  "tags": ["Work"],
  "created_at": "2025-12-29T09:00:00"
}
```

## API Contract Implications

### Task Creation
- All new fields are optional in creation (will use defaults)
- Validation must occur before saving
- created_at is automatically set to current timestamp

### Task Updates
- Individual fields can be updated independently
- Validation must occur for each updated field
- Other fields remain unchanged

### Task Retrieval
- All fields returned in response
- None values for optional fields are preserved
- Default values are returned for missing fields in old tasks