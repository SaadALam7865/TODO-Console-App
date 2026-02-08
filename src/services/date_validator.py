"""
Date Validation Service for Phase I - Advanced Features: Intelligent Automation

This module provides functions to validate date formats and check date validity
for both date-only and date-time formats needed for advanced features.
"""

from datetime import datetime
import re


def validate_date_format(date_string: str) -> bool:
    """
    Validate that the date string matches supported formats:
    - YYYY-MM-DD (date only)
    - YYYY-MM-DD HH:MM (date with time)
    - YYYY-MM-DDTHH:MM (ISO format with time)
    - YYYY-MM-DDTHH:MM:SS (ISO format with time and seconds)

    Args:
        date_string: The date string to validate

    Returns:
        True if the format is valid, False otherwise
    """
    if not date_string:
        return True  # Allow None/empty dates

    # Check if the format matches supported date formats
    # YYYY-MM-DD
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
        return True

    # YYYY-MM-DD HH:MM
    if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', date_string):
        return True

    # YYYY-MM-DDTHH:MM (ISO format)
    if re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$', date_string):
        return True

    # YYYY-MM-DDTHH:MM:SS (ISO format with seconds)
    if re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', date_string):
        return True

    return False


def validate_date_existence(date_string: str) -> bool:
    """
    Validate that the date string represents an actual calendar date/time.

    Args:
        date_string: The date string to validate

    Returns:
        True if the date exists, False otherwise
    """
    if not date_string:
        return True  # Allow None/empty dates

    # Try different supported formats
    formats = [
        "%Y-%m-%d",           # Date only
        "%Y-%m-%d %H:%M",     # Date with time
        "%Y-%m-%dT%H:%M",     # ISO format with time
        "%Y-%m-%dT%H:%M:%S"   # ISO format with time and seconds
    ]

    for fmt in formats:
        try:
            # This will raise ValueError if the date is invalid (e.g., Feb 30)
            datetime.strptime(date_string, fmt)
            return True
        except ValueError:
            continue

    return False


def is_valid_date(date_string: str) -> bool:
    """
    Validate that the date string is both properly formatted and represents a real date/time.

    Args:
        date_string: The date string to validate

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
    Check if the date is in the future compared to now.

    Args:
        date_string: The date string to check

    Returns:
        True if the date is in the future, False otherwise
    """
    if not date_string:
        return False  # No date is not in the future

    # Try different supported formats
    formats = [
        "%Y-%m-%d",           # Date only
        "%Y-%m-%d %H:%M",     # Date with time
        "%Y-%m-%dT%H:%M",     # ISO format with time
        "%Y-%m-%dT%H:%M:%S"   # ISO format with time and seconds
    ]

    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_string, fmt)
            now = datetime.now()
            return date_obj > now
        except ValueError:
            continue

    return False  # Invalid date is not in the future


def is_past_date(date_string: str) -> bool:
    """
    Check if the date is in the past compared to now.

    Args:
        date_string: The date string to check

    Returns:
        True if the date is in the past, False otherwise
    """
    if not date_string:
        return False  # No date is not in the past

    # Try different supported formats
    formats = [
        "%Y-%m-%d",           # Date only
        "%Y-%m-%d %H:%M",     # Date with time
        "%Y-%m-%dT%H:%M",     # ISO format with time
        "%Y-%m-%dT%H:%M:%S"   # ISO format with time and seconds
    ]

    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_string, fmt)
            now = datetime.now()
            return date_obj < now
        except ValueError:
            continue

    return False  # Invalid date is not in the past


def parse_datetime_string(date_string: str) -> datetime:
    """
    Parse a date string into a datetime object using the appropriate format.

    Args:
        date_string: The date string to parse

    Returns:
        datetime object if parsing is successful, None otherwise
    """
    if not date_string:
        return None

    # Try different supported formats
    formats = [
        "%Y-%m-%d",           # Date only
        "%Y-%m-%d %H:%M",     # Date with time
        "%Y-%m-%dT%H:%M",     # ISO format with time
        "%Y-%m-%dT%H:%M:%S"   # ISO format with time and seconds
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue

    return None


def is_valid_reminder_time(reminder_time: int) -> bool:
    """
    Validate that the reminder time is a positive integer.

    Args:
        reminder_time: The reminder time in minutes before due date

    Returns:
        True if the reminder time is valid, False otherwise
    """
    if reminder_time is None:
        return True  # Allow None for no reminder

    if isinstance(reminder_time, int) and reminder_time >= 0:
        return True

    return False