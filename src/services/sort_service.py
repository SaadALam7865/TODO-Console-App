"""
Sort Service for Phase I - Intermediate Features

This module provides functions to sort tasks by various criteria for the sort feature.
"""

from typing import List, Callable
from datetime import datetime


def sort_tasks_by_due_date(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks by due date.

    Args:
        tasks: The list of task objects to sort
        ascending: True for earliest first, False for latest first

    Returns:
        List of tasks sorted by due date
    """
    def sort_key(task):
        # Put tasks without due date at the end
        if not getattr(task, 'due_date', None):
            return datetime.max if ascending else datetime.min
        try:
            due_date = datetime.strptime(task.due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            # If date is invalid, put it at the end
            return datetime.max if ascending else datetime.min

    return sorted(tasks, key=sort_key, reverse=not ascending)


def sort_tasks_by_priority(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks by priority level.

    Args:
        tasks: The list of task objects to sort
        ascending: True for Low to High, False for High to Low

    Returns:
        List of tasks sorted by priority
    """
    # Priority order: Low (0), Medium (1), High (2) - for ascending
    priority_order = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    def sort_key(task):
        priority = getattr(task, 'priority', 'Medium')
        return priority_order.get(priority, 1)  # Default to Medium if not found

    return sorted(tasks, key=sort_key, reverse=not ascending)


def sort_tasks_alphabetically(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks alphabetically by title.

    Args:
        tasks: The list of task objects to sort
        ascending: True for A-Z, False for Z-A

    Returns:
        List of tasks sorted alphabetically by title
    """
    return sorted(tasks, key=lambda task: getattr(task, 'title', '').lower(), reverse=not ascending)


def sort_tasks_by_creation_order(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks by creation order (ID).

    Args:
        tasks: The list of task objects to sort
        ascending: True for oldest first, False for newest first

    Returns:
        List of tasks sorted by creation order
    """
    return sorted(tasks, key=lambda task: getattr(task, 'id', 0), reverse=not ascending)


def sort_tasks_by_completion_status(tasks: List, incomplete_first: bool = True) -> List:
    """
    Sort tasks by completion status.

    Args:
        tasks: The list of task objects to sort
        incomplete_first: True to show incomplete tasks first, False for complete tasks first

    Returns:
        List of tasks sorted by completion status
    """
    return sorted(tasks, key=lambda task: getattr(task, 'completed', False), reverse=not incomplete_first)


def sort_tasks_by_overdue_status(tasks: List, overdue_first: bool = False) -> List:
    """
    Sort tasks by overdue status.

    Args:
        tasks: The list of task objects to sort
        overdue_first: True to show overdue tasks first, False for non-overdue first

    Returns:
        List of tasks sorted by overdue status
    """
    def sort_key(task):
        # Check if task is overdue (has due date and is past due, and not completed)
        is_overdue = getattr(task, 'is_overdue', lambda: False)()
        return is_overdue if overdue_first else not is_overdue

    return sorted(tasks, key=sort_key)