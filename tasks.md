# Implementation Tasks: Phase I Advanced Features - Intelligent Automation

**Feature**: Recurring Tasks & Time Reminders/Notifications
**Spec**: [specs_history/spec_14_recurring_tasks.md](../specs_history/spec_14_recurring_tasks.md), [specs_history/spec_15_time_reminders_notifications.md](../specs_history/spec_15_time_reminders_notifications.md)
**Plan**: [specs_history/plan.md](../specs_history/plan.md)
**Generated**: 2026-01-02

## Summary

Implementation of two advanced intelligent features for the Evolution of Todo - Phase I application: (1) Recurring Tasks - allowing tasks to automatically regenerate after completion based on daily/weekly/monthly patterns, and (2) Time Reminders & Browser Notifications - enabling users to set specific times for browser notifications before due dates. These enhancements will extend the existing enhanced Task data model with additional fields while maintaining full backward compatibility with all 9 existing features (5 basic + 4 intermediate). The implementation will follow spec-driven development principles with 100% Claude Code generation from refined specifications.

## Dependencies

- Python 3.13+ with UV package manager
- Existing enhanced todo functionality with 9 features (5 basic + 4 intermediate)
- All specifications in specs_history/ directory (spec_14, spec_15)
- Required dependencies: plyer, APScheduler, python-dateutil

## Implementation Strategy

- **MVP First**: Enhanced data model with recurring tasks as minimum viable increment
- **Incremental Delivery**: Recurring tasks first, then time reminders/notifications
- **Backward Compatibility**: All existing functionality must continue working

---

## Phase 1: Setup Tasks

- [X] T001 Install required dependencies (plyer, APScheduler, python-dateutil) via UV
- [X] T002 Update requirements.txt with new dependencies (plyer, APScheduler, python-dateutil)
- [X] T003 [P] Create src/services/recurrence_service.py with empty structure
- [X] T004 [P] Create src/services/notification_service.py with empty structure
- [X] T005 [P] Create src/services/scheduler_service.py with empty structure
- [X] T006 [P] Create src/services/datetime_parser.py with empty structure

## Phase 2: Enhanced Data Model & Foundational Services

- [X] T007 [P] Update src/models/task.py to extend Task model with recurrence fields
- [X] T008 [P] Update src/models/task.py to extend Task model with reminder fields
- [X] T009 [P] Update src/services/date_validator.py to handle date-time format validation
- [X] T010 [P] Update src/services/filter_service.py to support new Task fields
- [X] T011 [P] Update src/services/search_service.py to support new Task fields
- [X] T012 [P] Update src/services/sort_service.py to support new Task fields
- [X] T013 [P] Create basic recurrence_service.py with pattern validation
- [X] T014 [P] Create basic notification_service.py with placeholder functions
- [X] T015 [P] Create basic scheduler_service.py with placeholder structure
- [X] T016 [P] Create basic datetime_parser.py with date-time parsing functions
- [X] T017 [P] Update src/main.py to import new service modules
- [X] T018 [P] Update src/cli/menu.py to prepare for new menu options
- [ ] T019 [P] Test backward compatibility with existing 9 features

## Phase 3: [US1] Recurring Tasks Implementation

**Goal**: Enable users to create tasks that automatically repeat on a specified schedule after completion

**Independent Test Criteria**:
- User can create a recurring task with daily/weekly/monthly pattern
- When marked complete, a new instance is created with updated due date
- Recurring tasks are clearly marked in the task list

### Tests (Optional)
- [ ] T020 [US1] Create test cases for recurring task creation and generation

### Implementation
- [X] T021 [US1] Implement recurrence pattern validation in recurrence_service.py
- [X] T022 [US1] Implement due date calculation logic for daily recurrence
- [X] T023 [US1] Implement due date calculation logic for weekly recurrence
- [X] T024 [US1] Implement due date calculation logic for monthly recurrence using dateutil
- [X] T025 [US1] Handle edge cases for month-end dates and leap years in recurrence calculations
- [X] T026 [US1] Implement recurrence end date validation and checking
- [X] T027 [US1] Update TaskManager to handle recurring task completion logic
- [X] T028 [US1] Implement automatic task generation when recurring task is marked complete
- [X] T029 [US1] Ensure new instances inherit all properties from parent task
- [X] T030 [US1] Set is_recurring_instance flag for generated tasks
- [X] T031 [US1] Set parent_task_id reference for generated tasks
- [X] T032 [US1] Update CLI menu to add recurrence options during task creation
- [X] T033 [US1] Update CLI menu to allow modification of recurrence settings
- [X] T034 [US1] Update task list display to show recurrence indicators [DAILY]/[WEEKLY]/[MONTHLY]
- [X] T035 [US1] Implement option to disable recurrence for existing tasks
- [X] T036 [US1] Test recurrence functionality with all patterns and edge cases

## Phase 4: [US2] Time Reminders & Notifications Implementation

**Goal**: Enable users to set specific times for reminders before due dates and deliver browser notifications

**Independent Test Criteria**:
- User can set reminder time in minutes before due date
- Browser notification appears at specified time before due date
- Background scheduler runs without blocking console operations

### Tests (Optional)
- [ ] T037 [US2] Create test cases for reminder scheduling and notification delivery

### Implementation
- [X] T038 [US2] Implement notification service using plyer library
- [X] T039 [US2] Implement notification permission handling and fallbacks
- [X] T040 [US2] Create background scheduler using APScheduler
- [X] T041 [US2] Implement non-blocking scheduler that doesn't interfere with console
- [X] T042 [US2] Create reminder checking logic to identify upcoming notifications
- [X] T043 [US2] Update TaskManager to track last_notification_sent timestamps
- [X] T044 [US2] Implement reminder time validation and calculation logic
- [X] T045 [US2] Update CLI menu to add reminder options during task creation
- [X] T046 [US2] Update CLI menu to allow modification of reminder settings
- [X] T047 [US2] Update task list display to show reminder status (REM: Xmin)
- [X] T048 [US2] Implement global notification settings toggle
- [X] T049 [US2] Test notification delivery with various reminder times
- [X] T050 [US2] Test scheduler performance with multiple reminders

## Phase 5: Polish & Cross-Cutting Concerns

- [X] T051 Update task string representation to show new recurrence and reminder indicators
- [X] T052 Add input validation for all new fields in CLI interface
- [ ] T053 Test backward compatibility with existing tasks after enhancements
- [ ] T054 Verify all 9 existing features continue to work with new enhancements
- [ ] T055 Update error handling for new features to prevent application crashes
- [ ] T056 Test performance with multiple recurring tasks and scheduled reminders
- [ ] T057 Update help text and user guidance for new features
- [ ] T058 Run comprehensive test of all 11 features (5 basic + 4 intermediate + 2 advanced)
- [ ] T059 Document any configuration requirements for notifications and scheduling
- [ ] T060 Final integration test ensuring all components work together seamlessly

---

## Dependencies

- **US1 (Recurring Tasks)** must be completed before US2 (Time Reminders) can fully function
- **Phase 1** must be completed before Phase 2 (dependencies: libraries installed)
- **Phase 2** must be completed before Phase 3 and Phase 4 (dependencies: enhanced Task model, services ready)

## Parallel Execution Examples

- Tasks T003-T006 can be executed in parallel (different service files)
- Tasks T007-T012 can be executed in parallel (different files, no interdependencies)
- Tasks T013-T016 can be executed in parallel (different service files)
- Tasks T022-T024 can be executed in parallel (date calculation functions)
- Tasks T038-T040 can be executed in parallel (different service components)

## Independent Test Criteria

- **US1**: User can create recurring tasks with daily/weekly/monthly patterns and see new instances generated after completion
- **US2**: User can set reminder times and receive browser notifications at specified times before due dates