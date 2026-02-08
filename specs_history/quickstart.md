# Quickstart Guide: Phase I Advanced Features - Intelligent Automation

## Overview

This guide covers the implementation and usage of the two advanced features added in Phase I:
1. **Recurring Tasks** - Tasks that automatically regenerate after completion
2. **Time Reminders & Notifications** - Browser notifications at specified times before due dates

The application now supports 11 total features (5 basic + 4 intermediate + 2 advanced) while maintaining full backward compatibility.

## Prerequisites

Before implementing the advanced features, ensure you have:
- Python 3.13+ installed
- UV package manager installed
- Required dependencies installed (plyer, APScheduler)

### Installing Dependencies

```bash
# Install plyer for cross-platform notifications
uv pip install plyer

# Install APScheduler for background scheduling
uv pip install APScheduler

# Install dateutil for advanced date calculations
uv pip install python-dateutil
```

## Implementation Order

### 1. Enhanced Data Model (Extended Task Model)
First, extend the existing Task model with advanced fields:
- Add recurrence_pattern (optional, string, values: "daily", "weekly", "monthly", None)
- Add recurrence_interval (optional, integer, default: 1)
- Add recurrence_end_date (optional, string, format: YYYY-MM-DD)
- Add reminder_time (optional, integer, minutes before due date)
- Add last_notification_sent (optional, string, ISO timestamp)
- Add is_recurring_instance (optional, boolean, default: False)
- Add parent_task_id (optional, integer, reference to parent task)

### 2. Recurring Tasks Feature (spec_14_recurring_tasks.md)
- Implement recurrence calculation service (dateutil.relativedelta for monthly calculations)
- Add recurrence pattern validation
- Implement recurring task generation on completion
- Update task creation interface to include recurrence options
- Update task display to show recurrence indicators

### 3. Time Reminders & Notifications Feature (spec_15_time_reminders_notifications.md)
- Implement notification service (using plyer for cross-platform notifications)
- Implement scheduler service (using APScheduler for background checks)
- Add time parsing service (enhanced date/time format support)
- Update task creation interface to include reminder options
- Implement notification permission handling

## Validation Requirements

### Input Validation
- Recurrence pattern validation ("daily", "weekly", "monthly", None)
- Recurrence interval validation (positive integer ≥ 1)
- Recurrence end date validation (YYYY-MM-DD format, after current due_date)
- Reminder time validation (positive integer representing minutes)
- Time format validation (YYYY-MM-DD HH:MM for due dates with time)

### Data Integrity
- Maintain backward compatibility with existing tasks
- Apply default values to existing tasks when accessing new fields
- Ensure all validation passes before saving data
- Preserve parent-child relationships in recurring task chains

## Display Formatting

### Task Display Enhancement
- Show recurrence pattern in brackets: [DAILY], [WEEKLY], [MONTHLY]
- Show reminder time: REM: 60min (for 60 minutes before due date)
- Show time in due dates when present (YYYY-MM-DD HH:MM format)
- Maintain readability with additional information
- Distinguish between original tasks and recurring instances

### Menu Updates
- Add new menu options for recurrence settings
- Add new menu options for reminder settings
- Maintain existing menu structure for basic features
- Add help text for new advanced features

## Testing Strategy

### Individual Feature Testing
1. Test recurring task functionality independently
2. Test time reminder and notification functionality independently
3. Test background scheduler operation
4. Test recurrence calculations (monthly edge cases, leap years)
5. Test notification delivery and permission handling

### Integration Testing
1. Test all 11 features work together
2. Test backward compatibility with existing tasks
3. Test that basic features still work after enhancements
4. Test combination of advanced features (recurring + reminder tasks)
5. Test background scheduler doesn't block console operations

### Regression Testing
- Verify all 9 previous features still work correctly
- Verify existing tasks display correctly with new fields
- Verify no performance degradation
- Verify console responsiveness with background scheduler

## Backward Compatibility Checklist

- [x] Existing task creation still works without new fields
- [x] Existing task viewing still works correctly
- [x] Existing task updating still works for original fields
- [x] Existing task deletion still works
- [x] Existing mark complete/incomplete still works
- [x] Tasks created before enhancement display correctly
- [x] No crashes when mixing old and new task formats
- [x] All 9 previous features continue to work unchanged
- [x] Due date format YYYY-MM-DD still supported
- [x] New time format YYYY-MM-DD HH:MM also supported

## Advanced Feature Usage

### Setting Up Recurring Tasks
1. When creating a task, select recurrence pattern (Daily/Weekly/Monthly/None)
2. Set recurrence interval (e.g., every 2 weeks, every 3 months)
3. Optionally set end date to limit recurrence
4. When marked complete, new instance automatically created with updated due date

### Setting Up Time Reminders
1. Set due date with time (YYYY-MM-DD HH:MM format)
2. Set reminder time in minutes before due date
3. On first notification, system requests browser permission
4. Notifications appear at calculated time (due date - reminder time)

### Managing Advanced Features
- Recurrence and reminder settings can be modified after task creation
- Recurring tasks show indicators in task list display
- Time-based reminders work with or without recurrence
- Background scheduler runs without blocking console operations

## Success Metrics

### Functional
- All 11 features (5 basic + 4 intermediate + 2 advanced) work correctly
- No regression in basic functionality
- Recurring tasks generate new instances properly
- Time reminders trigger notifications at correct times
- Background scheduler runs without blocking console
- Console interface remains responsive with advanced features

### Quality
- Input validation prevents all crashes
- Error messages are clear and helpful
- Display formatting remains readable with additional data
- Help documentation explains all features clearly
- Cross-platform notifications work reliably
- Recurrence calculations handle edge cases correctly

## Common Implementation Challenges

### Date Calculations
- Monthly recurrence requires special handling for month-end dates
- Leap years affect February 29th calculations
- Use dateutil.relativedelta for accurate monthly calculations

### Background Scheduling
- Scheduler must not block console input
- Handle scheduler startup and shutdown gracefully
- Manage memory usage of scheduled tasks

### Notification Permissions
- Handle cases where notifications are blocked by user
- Provide fallback options when notifications unavailable
- Request permissions appropriately during first use