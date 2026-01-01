"""
Priority Validation Service for Phase I - Intermediate Features

This module provides functions to validate priority values for the priority feature.
"""

from typing import List


def validate_priority(priority: str) -> bool:
    """
    Validate that the priority value is one of the allowed values.

    Args:
        priority: The priority string to validate

    Returns:
        True if the priority is valid, False otherwise
    """
    if not priority:
        return False

    valid_priorities = {"high", "medium", "low"}
    return priority.lower() in valid_priorities


def normalize_priority(priority: str) -> str:
    """
    Normalize the priority value to proper case (High, Medium, Low).

    Args:
        priority: The priority string to normalize

    Returns:
        Normalized priority string in proper case
    """
    if not priority:
        return "Medium"  # Default priority

    priority_lower = priority.lower()
    priority_mapping = {
        "high": "High",
        "medium": "Medium",
        "low": "Low"
    }

    return priority_mapping.get(priority_lower, "Medium")


def get_priority_order(priority: str) -> int:
    """
    Get the order value for a priority level for sorting purposes.

    Args:
        priority: The priority string

    Returns:
        Integer representing the priority order (High: 0, Medium: 1, Low: 2)
    """
    priority = normalize_priority(priority)
    priority_order = {
        "High": 0,
        "Medium": 1,
        "Low": 2
    }
    return priority_order.get(priority, 1)  # Default to Medium order if invalid


def get_all_valid_priorities() -> List[str]:
    """
    Get all valid priority values.

    Returns:
        List of valid priority strings
    """
    return ["High", "Medium", "Low"]