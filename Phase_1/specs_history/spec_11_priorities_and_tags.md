# Specification: Priorities and Tags/Categories Feature (Phase I - Intermediate)

## Feature Description
Enhance the todo console application with priority levels (High/Medium/Low) and tag/categories (Work/Home/Personal) functionality allowing users to assign, update, and filter tasks by priority and tags, with visual indicators in task displays.

## User Scenarios & Testing

### Primary User Flows
1. **Adding task with priority/tags**: User creates a new task and optionally specifies priority level and tags, with validation for allowed values
2. **Updating task priority/tags**: User modifies existing task to change priority level or add/remove tags
3. **Viewing tasks with priority/tags**: User sees priority levels and tags displayed in task lists with visual indicators
4. **Priority/tag validation**: User receives feedback for invalid priority levels or tag values

### Acceptance Scenarios
- User can add a task with priority level (High, Medium, or Low)
- User can add multiple tags to a task from allowed categories (Work, Home, Personal)
- User can update existing task priority and tags
- Default priority is Medium when not specified
- Default tags list is empty when not specified
- Invalid priority values are rejected with clear error messages
- Invalid tag values are rejected with clear error messages
- Priority and tags are displayed clearly in task lists

### Edge Cases
- Tasks created without priority default to Medium
- Tasks created without tags have empty tags list
- Multiple tags per task are supported
- Duplicate tags are handled appropriately (either prevented or consolidated)
- Priority values are case-insensitive or normalized
- Tag values are case-insensitive or normalized

## Functional Requirements

### FR-1: Priority Assignment
- System shall allow users to assign priority level to tasks: High, Medium, or Low
- Default priority level shall be Medium when not specified by user
- System shall validate priority values and reject invalid options (e.g., "Urgent", "Critical")
- Priority values shall be case-insensitive (HIGH, high, High all accepted as "High")
- System shall store priority as normalized value (proper case: High, Medium, Low)

### FR-2: Tag Assignment
- System shall allow users to assign tags from predefined categories: Work, Home, Personal
- System shall allow multiple tags per task
- Default tags list shall be empty when not specified by user
- System shall validate tag values and reject invalid categories
- Tag values shall be case-insensitive during input but stored in normalized form
- System shall prevent duplicate tags on same task (optional: either prevent or consolidate)

### FR-3: Update Priority and Tags
- System shall allow users to modify priority level of existing tasks
- System shall allow users to add or remove tags from existing tasks
- All validation rules from FR-1 and FR-2 apply to updates
- System shall preserve other task data when updating priority/tags only

### FR-4: Display Priority and Tags
- System shall display priority level in task lists with visual indicators (e.g., symbols or color coding)
- System shall display all tags for each task in a readable format
- Priority indicators shall be immediately recognizable (e.g., H/M/L prefixes or symbols)
- Tag display shall be compact but clear (e.g., [Work], [Home], [Personal])
- Default values (Medium priority, no tags) should be handled gracefully in display

### FR-5: Priority and Tag Validation
- System shall validate priority against allowed values: High, Medium, Low
- System shall validate tags against allowed categories: Work, Home, Personal
- Error messages shall clearly indicate valid options when invalid values are entered
- System shall provide helpful suggestions for typos (e.g., "wrok" suggests "Work")

## Non-Functional Requirements

### Performance
- Priority and tag validation shall complete in under 50ms
- Task list display performance shall not be significantly impacted by additional data
- Search and filtering by priority/tag shall be efficient for large task lists

### Usability
- Priority and tag options shall be clearly communicated to users
- Error messages shall suggest valid values when validation fails
- Visual indicators for priority shall be intuitive and distinguishable
- Tag display shall not overcrowd task list formatting

### Reliability
- Priority and tag values shall be consistently stored and retrieved
- Validation shall be applied consistently across all application functions
- Invalid priority/tag combinations shall be prevented from being stored

## Success Criteria

### Quantitative Metrics
- 100% of priority validation scenarios handled correctly (valid/invalid values)
- 100% of tag validation scenarios handled correctly (valid/invalid values)
- User completion rate for priority/tag operations above 95%
- Priority and tag display accuracy of 100%

### Qualitative Measures
- Users can successfully assign, update, and view tasks with priorities and tags
- Priority visual indicators are immediately recognizable
- Tag assignment is intuitive and flexible
- Integration with existing task features works seamlessly
- Console output remains readable with additional priority/tag information

### Business Outcomes
- Users can effectively categorize and prioritize tasks for better organization
- Task management becomes more effective with priority and category awareness
- Application demonstrates production-ready categorization capabilities

## Key Entities

### Task Entity Enhancement
- **priority**: String field with values: "High", "Medium", "Low", default: "Medium"
- **tags**: List/array of string values from: ["Work", "Home", "Personal"], default: []
- **priority_validator**: Function to validate priority against allowed values
- **tag_validator**: Function to validate tags against allowed categories

### System Dependencies
- Enhanced display formatting functions for priority and tag visualization
- Validation functions for priority and tag values
- Input processing functions to handle priority and tag assignment

## Constraints & Assumptions

### Technical Constraints
- Priority values limited to: High, Medium, Low
- Tag categories limited to: Work, Home, Personal
- Priority and tag values are case-insensitive during input
- Storage remains in-memory (no persistence changes required)
- Task data model extension must maintain backward compatibility

### Assumptions
- Users understand priority levels and will choose appropriate values
- The three priority levels (High/Medium/Low) are sufficient for user needs
- The three tag categories (Work/Home/Personal) cover most user categorization needs
- Basic task CRUD operations continue to function unchanged
- Console display can accommodate additional priority/tag information without overcrowding

## Risks & Mitigations

### Validation Risks
- Risk: Users enter invalid priority or tag values
- Mitigation: Comprehensive validation with clear error messages and value suggestions

### Display Risks
- Risk: Task lists become cluttered with priority/tag information
- Mitigation: Consistent formatting and compact visual indicators

### Expansion Risks
- Risk: Users want additional priority levels or tag categories
- Mitigation: Design with extensibility in mind for future enhancement

## Dependencies

### Internal Dependencies
- Existing Task data model requires extension to include priority and tags fields
- Task display functions require updates to show priority and tag information
- Input validation functions need priority and tag validation capabilities
- Menu systems may need updates to support priority/tag operations

### External Dependencies
- No external dependencies beyond existing Python standard library

## Scope

### In Scope
- Adding priority and tags to new tasks
- Updating priority and tags on existing tasks
- Validating priority and tag values
- Displaying priority and tags in task lists
- Handling default values for priority and tags
- Supporting multiple tags per task

### Out of Scope
- Custom priority levels beyond High/Medium/Low
- Custom tag categories beyond Work/Home/Personal
- Priority-based sorting (covered in separate sort feature)
- Tag-based filtering (covered in separate filter feature)
- Database persistence (remains in-memory)
- Web or mobile interface implementation
- Priority/tag statistics or analytics

## Assumptions

- Priority values will be stored as proper case (High, Medium, Low) internally
- Tags will be stored as proper case (Work, Home, Personal) internally
- Users will understand the meaning of High/Medium/Low priority levels
- The three tag categories will satisfy most user organizational needs
- Task data model extension will not break existing functionality
- Console display can accommodate priority and tag information within standard terminal widths