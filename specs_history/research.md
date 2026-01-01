# Research: Phase I Intermediate Features

## Decision 1: Date Format Standard

**Decision**: Use ISO format (YYYY-MM-DD)
**Rationale**: Provides consistency, enables easy sorting and comparison, and follows international standards. The format is unambiguous and easily parsed by Python's datetime module.
**Alternatives considered**:
- Multiple formats with parsing (MM/DD/YYYY, DD-MM-YYYY) - rejected due to ambiguity and complexity
- Natural language (today, tomorrow, next week) - rejected due to complexity and potential parsing errors

## Decision 2: Priority Implementation

**Decision**: String values ("High", "Medium", "Low")
**Rationale**: Provides clear, human-readable values that are easy to understand. Can be easily compared and sorted with a defined order. Simple to validate and display.
**Alternatives considered**:
- Numeric values (1, 2, 3) - rejected as less user-friendly
- Enum class for type safety - rejected as too complex for this phase

## Decision 3: Tags/Categories Structure

**Decision**: Multiple tags per task (list), predefined categories only
**Rationale**: Provides flexibility for users to categorize tasks in multiple ways while maintaining consistency with predefined categories. Prevents data inconsistency from free-form tags.
**Alternatives considered**:
- Single category per task - rejected as too limiting
- Free-form tags - rejected as it could lead to inconsistent tagging

## Decision 4: Search Algorithm

**Decision**: Case-insensitive substring match
**Rationale**: Provides good balance between precision and usability. Users can find tasks with partial matches regardless of case, which is intuitive.
**Alternatives considered**:
- Exact match only - rejected as too restrictive
- Fuzzy matching with similarity scores - rejected as too complex for this phase

## Decision 5: Filter Combination Logic

**Decision**: AND logic (all filters must match)
**Rationale**: Provides precise, predictable results. Users can narrow down results systematically by applying multiple filters.
**Alternatives considered**:
- OR logic (any filter matches) - rejected as it could return too many results
- User-selectable AND/OR - rejected as too complex for this phase

## Decision 6: Sort Persistence

**Decision**: Maintain sort preference during session
**Rationale**: Provides better user experience by maintaining the user's preferred view across operations within the same session.
**Alternatives considered**:
- Reset to default after each operation - rejected as inconvenient
- Save sort preference (requires persistence) - rejected as beyond Phase I scope

## Decision 7: Data Model Migration Strategy

**Decision**: Extend existing model with optional fields (backward compatible)
**Rationale**: Maintains all existing functionality while adding new features. Existing tasks without new fields will work correctly with default values.
**Alternatives considered**:
- Break existing basic implementation and rebuild - rejected as it violates backward compatibility
- Create new enhanced model, migrate data - rejected as unnecessarily complex

## Technical Implementation Notes

### Enhanced Task Structure
```python
{
  'id': int,
  'title': str,
  'description': str,
  'complete': bool,
  'due_date': str or None,  # Optional, ISO format YYYY-MM-DD
  'priority': str,          # 'High', 'Medium', 'Low', default 'Medium'
  'tags': list,             # ['Work', 'Home', 'Personal'], default []
  'created_at': str         # ISO timestamp for default sorting
}
```

### Validation Requirements
- Date validation: Check format and calendar validity
- Priority validation: Only accept "High", "Medium", "Low" (case-insensitive)
- Tag validation: Only accept "Work", "Home", "Personal" (case-insensitive), allow multiple
- Input validation: Prevent crashes from invalid user input

### Display Considerations
- Priority indicators: Use symbols (🔴 High, 🟡 Medium, 🟢 Low)
- Due date formatting: Show relative time when possible (e.g., "Due today", "Overdue")
- Tag display: Comma-separated list in brackets [Work, Personal]
- Sort indicator: Show current sort method to user