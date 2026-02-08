# Tasks: Todo In-Memory Python Console Application

## Feature Overview
Command-line todo manager with in-memory storage supporting basic CRUD operations (Add, View, Update, Delete, Mark Complete/Incomplete) following spec-driven development principles with 100% AI-assisted code generation.

## Implementation Strategy
- MVP: Implement basic Task class and Add/View features
- Incremental: Add remaining features one by one
- Test-driven: Each feature should be independently testable
- Spec-compliant: All code generated from specifications

## Dependencies
- Python 3.13+
- Standard library only (no external dependencies)

## Parallel Execution Examples
- [P] Tasks T005, T006, T007 can run in parallel (different UI functions)
- [P] Tests T025, T026, T027, T028, T029 can run in parallel (independent feature tests)

---

## Phase 1: Setup
**Goal**: Initialize project structure and basic configuration

- [ ] T001 Create project directory structure per implementation plan
- [ ] T002 Create requirements.txt with Python 3.13+ requirement
- [ ] T003 Create README.md with setup and usage instructions
- [ ] T004 Create CLAUDE.md documenting Claude Code interaction workflow

---

## Phase 2: Foundational
**Goal**: Create core data model and basic application structure

- [ ] T005 Create Task class in src/main.py with id, title, description, completed fields
- [ ] T006 Create TodoApp class in src/main.py with in-memory storage (dictionary)
- [ ] T007 Implement ID generation strategy (sequential integers starting from 1)
- [ ] T008 Create basic CLI menu structure in src/main.py
- [ ] T009 Implement input validation utilities for user input

---

## Phase 3: [US1] Add Task Feature
**Goal**: Implement ability to add tasks with title and description

**Independent Test Criteria**:
- Can create task with title only
- Can create task with title and description
- Generated ID is unique
- Task appears in view list after creation
- Empty title is rejected

- [ ] T010 [US1] Implement add_task method in TodoApp class
- [ ] T011 [US1] Add input validation to prevent empty titles
- [ ] T012 [US1] Implement unique ID generation for new tasks
- [ ] T013 [US1] Create CLI handler for Add Task menu option
- [ ] T014 [US1] Display confirmation message after successful addition
- [ ] T025 [P] [US1] Create test for Add Task feature

---

## Phase 4: [US2] View Tasks Feature
**Goal**: Implement ability to display all tasks with proper formatting

**Independent Test Criteria**:
- Empty list displays appropriate message
- Single task displays correctly
- Multiple tasks display with proper formatting
- Completion status visible (✓ or ✗)
- All task details shown (ID, title, description, status)

- [ ] T015 [US2] Implement view_tasks method in TodoApp class
- [ ] T016 [US2] Create proper display formatting for tasks
- [ ] T017 [US2] Show completion status with clear indicators ([ ] for incomplete, [x] for complete)
- [ ] T018 [US2] Create CLI handler for View Tasks menu option
- [ ] T026 [P] [US2] Create test for View Tasks feature

---

## Phase 5: [US3] Update Task Feature
**Goal**: Implement ability to modify existing task title or description

**Independent Test Criteria**:
- Can update title only
- Can update description only
- Can update both title and description
- Invalid ID shows error message
- Updated task reflects changes in view

- [ ] T019 [US3] Implement update_task method in TodoApp class
- [ ] T020 [US3] Add validation to check task ID exists before updating
- [ ] T021 [US3] Create CLI handler for Update Task menu option
- [ ] T022 [US3] Display confirmation message after successful update
- [ ] T027 [P] [US3] Create test for Update Task feature

---

## Phase 6: [US4] Delete Task Feature
**Goal**: Implement ability to remove tasks from memory by ID

**Independent Test Criteria**:
- Valid ID removes task successfully
- Invalid ID shows error message
- Deleted task no longer appears in view
- Delete confirmation prevents accidents

- [ ] T023 [US4] Implement delete_task method in TodoApp class
- [ ] T024 [US4] Add validation to check task ID exists before deletion
- [ ] T028 [P] [US4] Create test for Delete Task feature

---

## Phase 7: [US5] Mark Complete/Incomplete Feature
**Goal**: Implement ability to toggle task completion status

**Independent Test Criteria**:
- Can mark incomplete task as complete
- Can mark complete task as incomplete
- Status toggle reflected in view
- Invalid ID shows error message

- [ ] T029 [US5] Implement toggle_task_status method in TodoApp class
- [ ] T030 [US5] Add validation to check task ID exists before changing status
- [ ] T031 [US5] Create CLI handler for Mark Complete/Incomplete menu option
- [ ] T032 [US5] Display confirmation message after status change

---

## Phase 8: Polish & Cross-Cutting Concerns
**Goal**: Complete application with error handling, documentation, and testing

- [ ] T033 Add comprehensive error handling to prevent application crashes
- [ ] T034 Implement input validation across all user interaction points
- [ ] T035 Ensure console output is readable and well-formatted
- [ ] T036 Add docstrings and comments following Python conventions
- [ ] T037 Create comprehensive test script covering all 5 features
- [ ] T038 Verify all code follows PEP 8 style conventions
- [ ] T039 Update README.md with complete feature documentation
- [ ] T040 Final testing of all features working together