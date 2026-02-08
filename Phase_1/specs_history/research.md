# Research: Phase I Advanced Features - Intelligent Automation

## Decision 1: Recurrence Date Calculation

**Decision**: Use dateutil.relativedelta for monthly calculations and timedelta for daily/weekly
**Rationale**: reladelta properly handles month-end dates (e.g., Jan 31 + 1 month = Feb 28/29) and leap years, while timedelta handles simple day/week increments reliably
**Alternatives considered**:
- Simple arithmetic (date + 30 days) - rejected as it fails on month-end cases
- Manual date calculation - rejected as error-prone for edge cases
- dateutil.relativedelta (selected for robustness)

## Decision 2: Background Scheduler Implementation

**Decision**: Use APScheduler with background thread for non-blocking operations
**Rationale**: Provides reliable scheduling without blocking console input, handles complex scheduling scenarios, and has good error handling
**Alternatives considered**:
- Threading with time.sleep() - rejected as less robust and blocking
- APScheduler (selected for reliability and advanced features)
- Asyncio event loop - rejected as overkill for console app

## Decision 3: Browser Notification Approach

**Decision**: Use plyer library for cross-platform desktop notifications
**Rationale**: Simple interface to system notification systems across platforms (Windows, macOS, Linux)
**Alternatives considered**:
- Python plyer library (selected for cross-platform support)
- Web browser notifications via localhost server - rejected as unnecessary complexity
- OS-specific notification APIs - rejected as not cross-platform

## Decision 4: Recurring Task Completion Behavior

**Decision**: Immediate creation of new recurring task instances upon completion
**Rationale**: Ensures real-time continuity of recurring tasks, providing immediate visibility of next occurrence
**Alternatives considered**:
- Immediate creation (selected for real-time behavior)
- Scheduled creation at midnight - rejected as delayed behavior
- Creation on app launch - rejected as unreliable

## Decision 5: Time Format Handling

**Decision**: Support both date-only and date-time formats (YYYY-MM-DD and YYYY-MM-DD HH:MM)
**Rationale**: Maintains backward compatibility with existing features while enabling time-based reminders
**Alternatives considered**:
- Date-only (YYYY-MM-DD) - rejected as inadequate for time reminders
- Date-time only (YYYY-MM-DD HH:MM) - rejected as it would break existing functionality
- Both formats (selected for compatibility)

## Decision 6: Reminder Offset Units

**Decision**: Use minutes as base unit for reminder offsets with UI presets
**Rationale**: Provides precision while maintaining user-friendly interface with preset options (5min, 1hr, 1day)
**Alternatives considered**:
- Minutes only (selected for precision)
- Hours and minutes (more complex UI)
- Predefined options only - rejected as less flexible

## Decision 7: Task Model Extension Strategy

**Decision**: Extend existing Task model with optional fields for recurrence and reminders
**Rationale**: Maintains all existing functionality while adding new features. Existing tasks without new fields will work correctly with default values.
**Alternatives considered**:
- Separate recurring task model - rejected as it would complicate the codebase
- Extend existing model with optional fields (selected for simplicity)

## Technical Implementation Notes

### Enhanced Task Structure
```python
{
  'id': int,
  'title': str,
  'description': str,
  'complete': bool,
  'due_date': str or None,           # Optional, ISO format YYYY-MM-DD or YYYY-MM-DD HH:MM
  'priority': str,                   # 'High', 'Medium', 'Low', default 'Medium'
  'tags': list,                      # ['Work', 'Home', 'Personal'], default []
  'created_at': str,                 # ISO timestamp for default sorting
  'recurrence_pattern': str or None, # 'daily'/'weekly'/'monthly'/None, default None
  'recurrence_interval': int,        # Integer interval, default 1
  'recurrence_end_date': str or None, # Optional end date for recurrence, default None
  'reminder_time': int or None,      # Minutes before due date, default None
  'last_notification_sent': str or None, # Timestamp of last notification, default None
  'is_recurring_instance': bool,     # Boolean flag, default False
  'parent_task_id': int or None      # Reference to parent task, default None
}
```

### Service Module Requirements
- recurrence_service.py: Handle recurrence calculations and next instance creation
- notification_service.py: Manage browser notifications and permission handling
- scheduler_service.py: Background task scheduler for checking reminders and recurring tasks
- datetime_parser.py: Enhanced date/time parsing with time support

### Validation Requirements
- Recurrence validation: Only accept valid patterns ('daily', 'weekly', 'monthly', None)
- Reminder validation: Ensure reminder_time is positive integer when set
- Date validation: Handle both date-only and date-time formats
- Interval validation: Ensure recurrence_interval is positive integer
- End date validation: Ensure recurrence_end_date is after current due_date when set

### Display Considerations
- Recurrence indicators: Show recurrence pattern in task list (e.g., "[DAILY]", "[WEEKLY]")
- Reminder indicators: Show reminder time in task list (e.g., "REM: 60min before")
- Time formatting: Display time when present in due_date
- Recurring task chains: Show parent-child relationships when relevant