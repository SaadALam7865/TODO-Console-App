"""
Tag Management Service for Phase I - Intermediate Features

This module provides functions to validate and manage tags for the tags feature.
"""

from typing import List


def validate_tag(tag: str) -> bool:
    """
    Validate that the tag value is one of the allowed values.

    Args:
        tag: The tag string to validate

    Returns:
        True if the tag is valid, False otherwise
    """
    if not tag:
        return False

    valid_tags = {"work", "home", "personal"}
    return tag.lower() in valid_tags


def normalize_tag(tag: str) -> str:
    """
    Normalize the tag value to proper case (Work, Home, Personal).

    Args:
        tag: The tag string to normalize

    Returns:
        Normalized tag string in proper case
    """
    if not tag:
        return ""

    tag_lower = tag.lower()
    tag_mapping = {
        "work": "Work",
        "home": "Home",
        "personal": "Personal"
    }

    return tag_mapping.get(tag_lower, "")


def normalize_tags(tags: List[str]) -> List[str]:
    """
    Normalize a list of tags to proper case.

    Args:
        tags: The list of tag strings to normalize

    Returns:
        List of normalized tag strings in proper case
    """
    normalized = []
    for tag in tags:
        normalized_tag = normalize_tag(tag)
        if normalized_tag and normalized_tag not in normalized:
            normalized.append(normalized_tag)
    return normalized


def get_all_valid_tags() -> List[str]:
    """
    Get all valid tag values.

    Returns:
        List of valid tag strings
    """
    return ["Work", "Home", "Personal"]


def add_tag_to_list(tags: List[str], tag: str) -> List[str]:
    """
    Add a tag to the list if it's valid and doesn't already exist.

    Args:
        tags: The current list of tags
        tag: The tag to add

    Returns:
        Updated list of tags
    """
    normalized_tag = normalize_tag(tag)
    if not normalized_tag:
        return tags  # Return unchanged if tag is invalid

    updated_tags = tags.copy()
    if normalized_tag not in updated_tags:
        updated_tags.append(normalized_tag)

    return updated_tags


def remove_tag_from_list(tags: List[str], tag: str) -> List[str]:
    """
    Remove a tag from the list if it exists.

    Args:
        tags: The current list of tags
        tag: The tag to remove

    Returns:
        Updated list of tags
    """
    normalized_tag = normalize_tag(tag)
    if not normalized_tag:
        return tags  # Return unchanged if tag is invalid

    updated_tags = [t for t in tags if t != normalized_tag]
    return updated_tags


def filter_tasks_by_tag(tasks: List, tag: str) -> List:
    """
    Filter a list of tasks by a specific tag.

    Args:
        tasks: The list of task objects to filter
        tag: The tag to filter by

    Returns:
        List of tasks that contain the specified tag
    """
    normalized_tag = normalize_tag(tag)
    if not normalized_tag:
        return []

    return [task for task in tasks if normalized_tag in getattr(task, 'tags', [])]