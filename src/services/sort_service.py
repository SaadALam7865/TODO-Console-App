"""
Sort Service for Phase I - Advanced Features: Intelligent Automation

This module provides functions to sort tasks by various criteria for the sort feature,
including support for new fields like recurrence and reminders.
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
            # Handle both date-only and date-time formats
            due_date_str = task.due_date
            if " " in due_date_str:  # Contains time
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
            elif "T" in due_date_str and due_date_str.count(":") >= 1:  # ISO format with time
                if due_date_str.count(":") == 2:  # Includes seconds
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%dT%H:%M:%S")
                else:  # No seconds
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%dT%H:%M")
            else:  # Date only
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
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


def sort_tasks_by_recurrence_pattern(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks by recurrence pattern.

    Args:
        tasks: The list of task objects to sort
        ascending: True for alphabetical order (daily, monthly, weekly, None), False for reverse

    Returns:
        List of tasks sorted by recurrence pattern
    """
    pattern_order = {
        'daily': 0,
        'monthly': 1,
        'weekly': 2,
        None: 3  # Tasks without recurrence at the end
    }

    def sort_key(task):
        pattern = getattr(task, 'recurrence_pattern', None)
        return pattern_order.get(pattern, 4)  # Default to end if not found

    return sorted(tasks, key=sort_key, reverse=not ascending)


def sort_tasks_by_reminder_time(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks by reminder time (minutes before due date).

    Args:
        tasks: The list of task objects to sort
        ascending: True for shortest time first, False for longest time first

    Returns:
        List of tasks sorted by reminder time
    """
    def sort_key(task):
        reminder_time = getattr(task, 'reminder_time', None)
        if reminder_time is None:
            # Tasks without reminders go to the end
            return float('inf') if ascending else float('-inf')
        return reminder_time

    return sorted(tasks, key=sort_key, reverse=not ascending)


def sort_tasks_by_recurring_instance(tasks: List, original_first: bool = True) -> List:
    """
    Sort tasks by recurring instance status.

    Args:
        tasks: The list of task objects to sort
        original_first: True to show original tasks first, False for recurring instances first

    Returns:
        List of tasks sorted by recurring instance status
    """
    return sorted(tasks, key=lambda task: getattr(task, 'is_recurring_instance', False), reverse=not original_first)


def sort_tasks_by_recurrence_interval(tasks: List, ascending: bool = True) -> List:
    """
    Sort tasks by recurrence interval.

    Args:
        tasks: The list of task objects to sort
        ascending: True for smallest interval first, False for largest interval first

    Returns:
        List of tasks sorted by recurrence interval
    """
    def sort_key(task):
        interval = getattr(task, 'recurrence_interval', 1)
        return interval

    return sorted(tasks, key=sort_key, reverse=not ascending)