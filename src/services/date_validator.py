"""
Date Validation Service for Phase I - Intermediate Features

This module provides functions to validate date formats and check date validity
for the due date feature.
"""

from datetime import datetime
import re


def validate_date_format(date_string: str) -> bool:
    """
    Validate that the date string matches YYYY-MM-DD format.

    Args:
        date_string: The date string to validate

    Returns:
        True if the format is valid, False otherwise
    """
    if not date_string:
        return True  # Allow None/empty dates

    # Check if the format matches YYYY-MM-DD
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_string):
        return False

    return True


def validate_date_existence(date_string: str) -> bool:
    """
    Validate that the date string represents an actual calendar date.

    Args:
        date_string: The date string to validate (format: YYYY-MM-DD)

    Returns:
        True if the date exists, False otherwise
    """
    if not date_string:
        return True  # Allow None/empty dates

    try:
        # This will raise ValueError if the date is invalid (e.g., Feb 30)
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_date(date_string: str) -> bool:
    """
    Validate that the date string is both properly formatted and represents a real date.

    Args:
        date_string: The date string to validate (format: YYYY-MM-DD)

    Returns:
        True if the date is valid, False otherwise
    """
    if not date_string:
        return True  # Allow None/empty dates

    if not validate_date_format(date_string):
        return False

    return validate_date_existence(date_string)


def is_future_date(date_string: str) -> bool:
    """
    Check if the date is in the future compared to today.

    Args:
        date_string: The date string to check (format: YYYY-MM-DD)

    Returns:
        True if the date is in the future, False otherwise
    """
    if not date_string:
        return False  # No date is not in the future

    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        today = datetime.now().date()
        return date_obj.date() > today
    except ValueError:
        return False  # Invalid date is not in the future


def is_past_date(date_string: str) -> bool:
    """
    Check if the date is in the past compared to today.

    Args:
        date_string: The date string to check (format: YYYY-MM-DD)

    Returns:
        True if the date is in the past, False otherwise
    """
    if not date_string:
        return False  # No date is not in the past

    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        today = datetime.now().date()
        return date_obj.date() < today
    except ValueError:
        return False  # Invalid date is not in the past