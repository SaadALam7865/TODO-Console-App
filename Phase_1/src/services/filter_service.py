"""
Filter Service for Phase I - Advanced Features: Intelligent Automation

This module provides functions to filter tasks by various criteria for the filter feature,
including support for new fields like recurrence and reminders.
"""

from typing import List


def filter_tasks_by_status(tasks: List, completed: bool = None) -> List:
    """
    Filter tasks by completion status.

    Args:
        tasks: The list of task objects to filter
        completed: True for completed tasks, False for incomplete tasks, None for all tasks

    Returns:
        List of tasks that match the status criteria
    """
    if completed is None:
        return tasks

    return [task for task in tasks if getattr(task, 'completed', False) == completed]


def filter_tasks_by_priority(tasks: List, priority: str = None) -> List:
    """
    Filter tasks by priority level.

    Args:
        tasks: The list of task objects to filter
        priority: The priority level to filter by ("High", "Medium", "Low")

    Returns:
        List of tasks that match the priority criteria
    """
    if not priority:
        return tasks

    # Normalize the priority to proper case
    priority_normalized = priority.capitalize()
    valid_priorities = {"High", "Medium", "Low"}

    if priority_normalized not in valid_priorities:
        return []  # Return empty list if priority is invalid

    return [task for task in tasks if getattr(task, 'priority', 'Medium') == priority_normalized]


def filter_tasks_by_tag(tasks: List, tag: str = None) -> List:
    """
    Filter tasks by tag.

    Args:
        tasks: The list of task objects to filter
        tag: The tag to filter by

    Returns:
        List of tasks that have the specified tag
    """
    if not tag:
        return tasks

    # Normalize the tag to proper case
    tag_normalized = tag.capitalize()
    valid_tags = {"Work", "Home", "Personal"}

    if tag_normalized not in valid_tags:
        return []  # Return empty list if tag is invalid

    return [task for task in tasks if tag_normalized in getattr(task, 'tags', [])]


def filter_tasks_by_due_date_status(tasks: List, status: str = None) -> List:
    """
    Filter tasks by due date status.

    Args:
        tasks: The list of task objects to filter
        status: The due date status to filter by ("overdue", "has_due_date", "no_due_date")

    Returns:
        List of tasks that match the due date status criteria
    """
    if not status:
        return tasks

    status_lower = status.lower()

    if status_lower == "overdue":
        # Tasks that have a due date in the past and are not completed
        return [task for task in tasks if getattr(task, 'is_overdue', lambda: False)()]
    elif status_lower == "has_due_date":
        # Tasks that have a due date set
        return [task for task in tasks if getattr(task, 'due_date', None) is not None]
    elif status_lower == "no_due_date":
        # Tasks that do not have a due date set
        return [task for task in tasks if getattr(task, 'due_date', None) is None]
    else:
        return tasks  # Return all tasks if status is invalid


def filter_tasks_by_recurrence_pattern(tasks: List, pattern: str = None) -> List:
    """
    Filter tasks by recurrence pattern.

    Args:
        tasks: The list of task objects to filter
        pattern: The recurrence pattern to filter by ("daily", "weekly", "monthly", None)

    Returns:
        List of tasks that match the recurrence pattern criteria
    """
    if pattern is None:
        return tasks

    # Normalize the pattern to lowercase
    pattern_lower = pattern.lower()
    valid_patterns = {"daily", "weekly", "monthly", "none", ""}

    if pattern_lower not in valid_patterns:
        return []  # Return empty list if pattern is invalid

    # Convert empty string to None for comparison
    if pattern_lower == "none" or pattern_lower == "":
        pattern_lower = None

    return [task for task in tasks if getattr(task, 'recurrence_pattern', None) == pattern_lower]


def filter_tasks_by_reminder_status(tasks: List, has_reminder: bool = None) -> List:
    """
    Filter tasks by reminder status.

    Args:
        tasks: The list of task objects to filter
        has_reminder: True for tasks with reminders, False for tasks without reminders, None for all tasks

    Returns:
        List of tasks that match the reminder status criteria
    """
    if has_reminder is None:
        return tasks

    if has_reminder:
        # Tasks that have a reminder_time set (not None)
        return [task for task in tasks if getattr(task, 'reminder_time', None) is not None]
    else:
        # Tasks that do not have a reminder_time set
        return [task for task in tasks if getattr(task, 'reminder_time', None) is None]


def filter_tasks_by_recurring_instance(tasks: List, is_instance: bool = None) -> List:
    """
    Filter tasks by recurring instance status.

    Args:
        tasks: The list of task objects to filter
        is_instance: True for recurring instances, False for original tasks, None for all tasks

    Returns:
        List of tasks that match the recurring instance criteria
    """
    if is_instance is None:
        return tasks

    return [task for task in tasks if getattr(task, 'is_recurring_instance', False) == is_instance]


def filter_tasks_by_combined_criteria(tasks: List, completed: bool = None,
                                priority: str = None, tag: str = None,
                                due_date_status: str = None,
                                recurrence_pattern: str = None,
                                has_reminder: bool = None,
                                is_instance: bool = None) -> List:
    """
    Filter tasks by multiple criteria using AND logic.

    Args:
        tasks: The list of task objects to filter
        completed: Filter by completion status
        priority: Filter by priority level
        tag: Filter by tag
        due_date_status: Filter by due date status
        recurrence_pattern: Filter by recurrence pattern
        has_reminder: Filter by reminder status
        is_instance: Filter by recurring instance status

    Returns:
        List of tasks that match all specified criteria
    """
    filtered_tasks = tasks

    # Apply each filter in sequence
    if completed is not None:
        filtered_tasks = filter_tasks_by_status(filtered_tasks, completed)

    if priority:
        filtered_tasks = filter_tasks_by_priority(filtered_tasks, priority)

    if tag:
        filtered_tasks = filter_tasks_by_tag(filtered_tasks, tag)

    if due_date_status:
        filtered_tasks = filter_tasks_by_due_date_status(filtered_tasks, due_date_status)

    if recurrence_pattern is not None:
        filtered_tasks = filter_tasks_by_recurrence_pattern(filtered_tasks, recurrence_pattern)

    if has_reminder is not None:
        filtered_tasks = filter_tasks_by_reminder_status(filtered_tasks, has_reminder)

    if is_instance is not None:
        filtered_tasks = filter_tasks_by_recurring_instance(filtered_tasks, is_instance)

    return filtered_tasks