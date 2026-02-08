"""
Search Service for Phase I - Advanced Features: Intelligent Automation

This module provides functions to search tasks by keywords for the search feature,
including support for new fields like recurrence and reminders.
"""

from typing import List


def search_tasks_by_keyword(tasks: List, keyword: str) -> List:
    """
    Search tasks by keyword in title, description, and tags.

    Args:
        tasks: The list of task objects to search
        keyword: The keyword to search for

    Returns:
        List of tasks that match the keyword
    """
    if not keyword:
        return []

    keyword_lower = keyword.lower()
    matching_tasks = []

    for task in tasks:
        title = getattr(task, 'title', '')
        description = getattr(task, 'description', '')
        tags = getattr(task, 'tags', [])

        # Check if keyword is in title or description (case-insensitive)
        if keyword_lower in title.lower() or keyword_lower in description.lower():
            matching_tasks.append(task)
            continue  # Found a match, continue to next task

        # Check if keyword is in any of the tags (case-insensitive)
        for tag in tags:
            if keyword_lower in tag.lower():
                matching_tasks.append(task)
                break  # Found a match in tags, continue to next task

    return matching_tasks


def search_tasks_by_title(tasks: List, keyword: str) -> List:
    """
    Search tasks by keyword in title only.

    Args:
        tasks: The list of task objects to search
        keyword: The keyword to search for

    Returns:
        List of tasks that match the keyword in title
    """
    if not keyword:
        return []

    keyword_lower = keyword.lower()
    matching_tasks = []

    for task in tasks:
        title = getattr(task, 'title', '')
        if keyword_lower in title.lower():
            matching_tasks.append(task)

    return matching_tasks


def search_tasks_by_description(tasks: List, keyword: str) -> List:
    """
    Search tasks by keyword in description only.

    Args:
        tasks: The list of task objects to search
        keyword: The keyword to search for

    Returns:
        List of tasks that match the keyword in description
    """
    if not keyword:
        return []

    keyword_lower = keyword.lower()
    matching_tasks = []

    for task in tasks:
        description = getattr(task, 'description', '')
        if keyword_lower in description.lower():
            matching_tasks.append(task)

    return matching_tasks


def search_tasks_by_tag(tasks: List, tag: str) -> List:
    """
    Search tasks by tag.

    Args:
        tasks: The list of task objects to search
        tag: The tag to search for

    Returns:
        List of tasks that have the specified tag
    """
    if not tag:
        return []

    tag_lower = tag.lower()
    matching_tasks = []

    for task in tasks:
        tags = getattr(task, 'tags', [])
        # Check if the tag exists in the task's tags list (case-insensitive)
        for task_tag in tags:
            if tag_lower == task_tag.lower():
                matching_tasks.append(task)
                break  # Found a match, no need to check other tags

    return matching_tasks


def search_tasks_by_recurrence_pattern(tasks: List, pattern: str) -> List:
    """
    Search tasks by recurrence pattern.

    Args:
        tasks: The list of task objects to search
        pattern: The recurrence pattern to search for ("daily", "weekly", "monthly")

    Returns:
        List of tasks that match the recurrence pattern
    """
    if not pattern:
        return []

    pattern_lower = pattern.lower()
    valid_patterns = {"daily", "weekly", "monthly"}

    if pattern_lower not in valid_patterns:
        return []  # Return empty list if pattern is invalid

    matching_tasks = []

    for task in tasks:
        task_pattern = getattr(task, 'recurrence_pattern', None)
        if task_pattern and task_pattern.lower() == pattern_lower:
            matching_tasks.append(task)

    return matching_tasks


def search_tasks_by_reminder_time(tasks: List, min_minutes: int = None, max_minutes: int = None) -> List:
    """
    Search tasks by reminder time range.

    Args:
        tasks: The list of task objects to search
        min_minutes: Minimum reminder time in minutes before due date
        max_minutes: Maximum reminder time in minutes before due date

    Returns:
        List of tasks with reminder time in the specified range
    """
    matching_tasks = []

    for task in tasks:
        reminder_time = getattr(task, 'reminder_time', None)
        if reminder_time is None:
            continue  # Skip tasks without reminders

        # Check if reminder time is within the specified range
        if min_minutes is not None and reminder_time < min_minutes:
            continue
        if max_minutes is not None and reminder_time > max_minutes:
            continue

        matching_tasks.append(task)

    return matching_tasks


def search_tasks_by_recurring_instance(tasks: List, is_instance: bool) -> List:
    """
    Search tasks by recurring instance status.

    Args:
        tasks: The list of task objects to search
        is_instance: True to find recurring instances, False to find original tasks

    Returns:
        List of tasks that match the recurring instance status
    """
    matching_tasks = []

    for task in tasks:
        task_is_instance = getattr(task, 'is_recurring_instance', False)
        if task_is_instance == is_instance:
            matching_tasks.append(task)

    return matching_tasks


def search_tasks_by_priority(tasks: List, priority: str) -> List:
    """
    Search tasks by priority level.

    Args:
        tasks: The list of task objects to search
        priority: The priority level to search for ("High", "Medium", "Low")

    Returns:
        List of tasks that match the priority level
    """
    if not priority:
        return []

    priority_lower = priority.lower()
    valid_priorities = {"high", "medium", "low"}

    if priority_lower not in valid_priorities:
        return []  # Return empty list if priority is invalid

    matching_tasks = []

    for task in tasks:
        task_priority = getattr(task, 'priority', 'medium')
        if task_priority.lower() == priority_lower:
            matching_tasks.append(task)

    return matching_tasks