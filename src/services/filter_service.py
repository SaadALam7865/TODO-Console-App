"""
Filter Service for Phase I - Intermediate Features

This module provides functions to filter tasks by various criteria for the filter feature.
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


def filter_tasks_by_combined_criteria(tasks: List, completed: bool = None,
                                   priority: str = None, tag: str = None,
                                   due_date_status: str = None) -> List:
    """
    Filter tasks by multiple criteria using AND logic.

    Args:
        tasks: The list of task objects to filter
        completed: Filter by completion status
        priority: Filter by priority level
        tag: Filter by tag
        due_date_status: Filter by due date status

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

    return filtered_tasks