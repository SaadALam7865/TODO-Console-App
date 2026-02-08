"""
DateTime Parser Service for Phase I Advanced Features

This module provides functionality for parsing and validating date-time strings
with support for both date-only and date-time formats.
"""

from datetime import datetime
from typing import Optional, Union
import re


class DateTimeParser:
    """Service class for parsing and validating date-time strings."""

    # Define supported date formats
    DATE_FORMATS = [
        "%Y-%m-%d",           # YYYY-MM-DD
        "%Y-%m-%d %H:%M",     # YYYY-MM-DD HH:MM
        "%Y-%m-%dT%H:%M",     # YYYY-MM-DDTHH:MM (ISO format)
        "%Y-%m-%dT%H:%M:%S",  # YYYY-MM-DDTHH:MM:SS (ISO format with seconds)
    ]

    TIME_FORMATS = [
        "%H:%M",              # HH:MM 24-hour format
        "%I:%M %p",           # HH:MM AM/PM format
        "%H:%M:%S",           # HH:MM:SS 24-hour format with seconds
        "%I:%M:%S %p",        # HH:MM:SS AM/PM format with seconds
    ]

    @staticmethod
    def parse_datetime(date_string: str) -> Optional[datetime]:
        """
        Parse a date-time string into a datetime object.

        Args:
            date_string: The date-time string to parse

        Returns:
            datetime object if parsing successful, None otherwise
        """
        if not date_string or not isinstance(date_string, str):
            return None

        # Try each supported format
        for fmt in DateTimeParser.DATE_FORMATS:
            try:
                return datetime.strptime(date_string.strip(), fmt)
            except ValueError:
                continue

        return None

    @staticmethod
    def parse_date_only(date_string: str) -> Optional[datetime]:
        """
        Parse a date-only string into a datetime object (time set to 00:00).

        Args:
            date_string: The date string to parse

        Returns:
            datetime object if parsing successful, None otherwise
        """
        if not date_string or not isinstance(date_string, str):
            return None

        # Only try date-only formats
        date_formats = ["%Y-%m-%d"]
        for fmt in date_formats:
            try:
                return datetime.strptime(date_string.strip(), fmt)
            except ValueError:
                continue

        return None

    @staticmethod
    def parse_time_only(time_string: str) -> Optional[datetime.time]:
        """
        Parse a time-only string into a time object.

        Args:
            time_string: The time string to parse

        Returns:
            time object if parsing successful, None otherwise
        """
        if not time_string or not isinstance(time_string, str):
            return None

        # Try each supported time format
        for fmt in DateTimeParser.TIME_FORMATS:
            try:
                parsed_datetime = datetime.strptime(time_string.strip(), fmt)
                return parsed_datetime.time()
            except ValueError:
                continue

        return None

    @staticmethod
    def format_datetime(dt: datetime, include_time: bool = True) -> str:
        """
        Format a datetime object into a string.

        Args:
            dt: The datetime object to format
            include_time: Whether to include time in the output

        Returns:
            Formatted date-time string
        """
        if include_time:
            # Check if time component has meaningful values
            if dt.time() != datetime.min.time():
                return dt.strftime("%Y-%m-%d %H:%M")
            else:
                return dt.strftime("%Y-%m-%d")
        else:
            return dt.strftime("%Y-%m-%d")

    @staticmethod
    def validate_date_format(date_string: str) -> bool:
        """
        Validate if a date string matches supported formats.

        Args:
            date_string: The date string to validate

        Returns:
            True if valid format, False otherwise
        """
        return DateTimeParser.parse_datetime(date_string) is not None

    @staticmethod
    def validate_date_range(
        date_string: str,
        min_date: Optional[datetime] = None,
        max_date: Optional[datetime] = None
    ) -> bool:
        """
        Validate if a date falls within a specified range.

        Args:
            date_string: The date string to validate
            min_date: Minimum allowed date (optional)
            max_date: Maximum allowed date (optional)

        Returns:
            True if date is in range, False otherwise
        """
        parsed_date = DateTimeParser.parse_datetime(date_string)
        if parsed_date is None:
            return False

        if min_date and parsed_date < min_date:
            return False

        if max_date and parsed_date > max_date:
            return False

        return True

    @staticmethod
    def is_valid_datetime_input(user_input: str) -> tuple[bool, str]:
        """
        Validate user input for date-time and provide feedback.

        Args:
            user_input: The user input string

        Returns:
            Tuple of (is_valid, feedback_message)
        """
        if not user_input or not isinstance(user_input, str):
            return False, "Date/time cannot be empty"

        # Check if it matches any supported format
        parsed = DateTimeParser.parse_datetime(user_input)
        if parsed is None:
            return False, f"Invalid date/time format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM"

        # Check if it's a valid calendar date
        try:
            # This will raise ValueError for invalid dates like Feb 30
            test_parse = datetime.strptime(user_input.strip().split()[0], "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date - not a real calendar date"

        return True, "Valid date/time format"

    @staticmethod
    def normalize_datetime_string(date_string: str) -> Optional[str]:
        """
        Normalize a date string to the standard format (YYYY-MM-DD or YYYY-MM-DD HH:MM).

        Args:
            date_string: The date string to normalize

        Returns:
            Normalized date string, or None if invalid
        """
        parsed = DateTimeParser.parse_datetime(date_string)
        if parsed is None:
            return None

        # Return in standard format
        if parsed.time() == datetime.min.time():
            # Date only
            return parsed.strftime("%Y-%m-%d")
        else:
            # Include time
            return parsed.strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def calculate_time_difference(
        start_time: str,
        end_time: str
    ) -> Optional[tuple[int, int, int]]:
        """
        Calculate the difference between two time strings.

        Args:
            start_time: Starting time string
            end_time: Ending time string

        Returns:
            Tuple of (days, hours, minutes) difference, or None if invalid
        """
        start_dt = DateTimeParser.parse_datetime(start_time)
        end_dt = DateTimeParser.parse_datetime(end_time)

        if start_dt is None or end_dt is None:
            return None

        diff = end_dt - start_dt
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        return days, hours, minutes

    @staticmethod
    def add_time_to_datetime(
        date_string: str,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0
    ) -> Optional[str]:
        """
        Add time to a date string and return the result.

        Args:
            date_string: The date string to add time to
            days: Number of days to add
            hours: Number of hours to add
            minutes: Number of minutes to add

        Returns:
            New date string with added time, or None if invalid
        """
        dt = DateTimeParser.parse_datetime(date_string)
        if dt is None:
            return None

        new_dt = dt + timedelta(days=days, hours=hours, minutes=minutes)
        return DateTimeParser.format_datetime(new_dt)


# Import required for timedelta in the last method
from datetime import timedelta