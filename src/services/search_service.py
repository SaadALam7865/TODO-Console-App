"""
Search Service for Phase I - Intermediate Features

This module provides functions to search tasks by keywords for the search feature.
"""

from typing import List


def search_tasks_by_keyword(tasks: List, keyword: str) -> List:
    """
    Search tasks by keyword in title and description.

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

        # Check if keyword is in title or description (case-insensitive)
        if keyword_lower in title.lower() or keyword_lower in description.lower():
            matching_tasks.append(task)

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