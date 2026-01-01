# Implementation Tasks: Phase I - Intermediate Level: Organization & Usability Enhancements

**Feature**: Evolution of Todo - Phase I Intermediate Features
**Spec**: [specs_history/intermediate_features_summary.md](../specs_history/intermediate_features_summary.md)
**Plan**: [specs_history/plan.md](../specs_history/plan.md)
**Generated**: 2026-01-01

## Summary

Implementation of four intermediate-level features for the Evolution of Todo - Phase I application: due dates, priorities/tags, search/filter, and sort functionality. These enhancements will extend the existing Task data model with new fields (due_date, priority, tags, created_at) while maintaining backward compatibility with the existing 5 basic features. The implementation will follow spec-driven development principles with 100% Claude Code generation from refined specifications.

## Dependencies

- Python 3.13+ with UV package manager
- Existing basic todo functionality in src/main.py
- All specifications in specs_history/ directory

## Implementation Strategy

- **MVP First**: Enhanced data model with due dates as minimum viable increment
- **Incremental Delivery**: Each feature builds on the enhanced data model
- **Backward Compatibility**: All existing functionality must continue working

---

## Phase 1: Setup Tasks

- [X] T001 Create project structure per implementation plan with models/, services/, cli/ directories
- [X] T002 [P] Create src/models directory and initial task.py file
- [X] T003 [P] Create src/services directory for validation and processing functions
- [X] T004 [P] Create src/cli directory for enhanced menu system

## Phase 2: Foundational Tasks

- [X] T005 Implement enhanced Task model with due_date, priority, tags, created_at fields in src/models/task.py
- [X] T006 Create date validation service in src/services/date_validator.py
- [X] T007 Create priority validation service in src/services/priority_validator.py
- [X] T008 Create tag management service in src/services/tag_manager.py
- [X] T009 Update main.py to use enhanced Task model while maintaining backward compatibility

## Phase 3: [US1] Due Dates Feature

- [X] T010 [P] [US1] Implement due date validation logic in src/services/date_validator.py
- [X] T011 [US1] Add due date functionality to Task model in src/models/task.py
- [X] T012 [P] [US1] Create add task with due date functionality in main.py
- [X] T013 [P] [US1] Create update task due date functionality in main.py
- [X] T014 [US1] Implement overdue status calculation in Task model
- [X] T015 [US1] Update task display to show due dates and overdue indicators in main.py
- [X] T016 [US1] Add due date input validation to user interface in main.py
- [X] T017 [US1] Test due date functionality with various date scenarios

## Phase 4: [US2] Priorities & Tags Feature

- [X] T018 [P] [US2] Implement priority validation logic in src/services/priority_validator.py
- [X] T019 [P] [US2] Implement tag validation logic in src/services/tag_manager.py
- [X] T020 [US2] Add priority and tags functionality to Task model in src/models/task.py
- [X] T021 [US2] Create add task with priority/tags functionality in main.py
- [X] T022 [US2] Create update task priority/tags functionality in main.py
- [X] T023 [US2] Update task display to show priority and tags indicators in main.py
- [X] T024 [US2] Add priority and tags input validation to user interface in main.py
- [X] T025 [US2] Test priority and tags functionality with various scenarios

## Phase 5: [US3] Search & Filter Feature

- [X] T026 [P] [US3] Create search service in src/services/search_service.py
- [X] T027 [P] [US3] Create filter service in src/services/filter_service.py
- [X] T028 [US3] Implement keyword search functionality in search service
- [X] T029 [US3] Implement status filtering functionality in filter service
- [X] T030 [US3] Implement priority filtering functionality in filter service
- [X] T031 [US3] Implement tag filtering functionality in filter service
- [X] T032 [US3] Implement combined filtering with AND logic in filter service
- [X] T033 [US3] Integrate search and filter into main.py menu system
- [X] T034 [US3] Update task display to work with filtered results in main.py
- [X] T035 [US3] Test search and filter functionality with various scenarios

## Phase 6: [US4] Sort Tasks Feature

- [X] T036 [P] [US4] Create sort service in src/services/sort_service.py
- [X] T037 [US4] Implement due date sorting functionality in sort service
- [X] T038 [US4] Implement priority sorting functionality in sort service
- [X] T039 [US4] Implement alphabetical sorting functionality in sort service
- [X] T040 [US4] Implement creation order sorting functionality in sort service
- [X] T041 [US4] Implement completion status sorting functionality in sort service
- [X] T042 [US4] Implement ascending/descending toggle functionality in sort service
- [X] T043 [US4] Integrate sort functionality into main.py menu system
- [X] T044 [US4] Update task display to show current sort method in main.py
- [X] T045 [US4] Test sort functionality with various scenarios

## Phase 7: Polish & Cross-Cutting Concerns

- [X] T046 Update CLI menu to include all new functionality in src/cli/menu.py
- [X] T047 Add comprehensive error handling for all new features in main.py
- [X] T048 Update user help and documentation in main.py
- [X] T049 Test full integration ensuring all 9 features work together
- [X] T050 Verify backward compatibility with existing basic features
- [X] T051 Performance test with multiple tasks and features enabled
- [X] T052 Code cleanup and documentation updates

---

## Dependencies

- **US1 (Due Dates)** must be completed before US3 (Search & Filter) and US4 (Sort) can fully function
- **US2 (Priorities & Tags)** must be completed before US3 (Search & Filter) and US4 (Sort) can fully function
- **US3 (Search & Filter)** and **US4 (Sort)** can be developed in parallel once US1 and US2 are complete

## Parallel Execution Examples

- Tasks T002, T003, T004 can be executed in parallel (creating directory structure)
- Tasks T010, T018, T026 can be executed in parallel (different service modules)
- Tasks T012, T013, T021, T022 can be executed in parallel (different functionality in main.py)

## Independent Test Criteria

- **US1**: User can add, update, view tasks with due dates and see overdue indicators
- **US2**: User can add, update, view tasks with priority levels and tags
- **US3**: User can search tasks by keyword and filter by various criteria
- **US4**: User can sort tasks by various criteria with ascending/descending options