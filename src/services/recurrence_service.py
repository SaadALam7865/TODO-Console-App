"""
Recurrence Service for Phase I Advanced Features

This module provides functionality for handling recurring tasks,
including pattern validation, due date calculations, and recurrence logic.
"""

from datetime import datetime, timedelta
from typing import Optional
from dateutil.relativedelta import relativedelta


class RecurrenceService:
    """Service class for handling recurring task calculations and logic."""

    VALID_PATTERNS = ['daily', 'weekly', 'monthly', None]

    @staticmethod
    def validate_pattern(pattern: Optional[str]) -> bool:
        """
        Validate if the recurrence pattern is valid.

        Args:
            pattern: The recurrence pattern to validate

        Returns:
            True if valid, False otherwise
        """
        return pattern in RecurrenceService.VALID_PATTERNS

    @staticmethod
    def validate_interval(interval: int) -> bool:
        """
        Validate if the recurrence interval is valid.

        Args:
            interval: The recurrence interval to validate

        Returns:
            True if valid (positive integer), False otherwise
        """
        return isinstance(interval, int) and interval >= 1

    @staticmethod
    def validate_end_date(end_date: Optional[str], current_due_date: Optional[str]) -> bool:
        """
        Validate if the recurrence end date is valid.

        Args:
            end_date: The end date to validate
            current_due_date: The current due date for comparison

        Returns:
            True if valid, False otherwise
        """
        if end_date is None:
            return True

        # Validate date format and ensure end_date is after current_due_date
        try:
            from datetime import datetime
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")

            if current_due_date:
                current_dt = datetime.strptime(current_due_date, "%Y-%m-%d")
                return end_dt.date() >= current_dt.date()
            else:
                return True
        except ValueError:
            return False

    @staticmethod
    def calculate_next_due_date(
        current_due_date: str,
        pattern: str,
        interval: int = 1
    ) -> Optional[str]:
        """
        Calculate the next due date based on the recurrence pattern and interval.

        Args:
            current_due_date: The current due date in YYYY-MM-DD format
            pattern: The recurrence pattern ('daily', 'weekly', 'monthly')
            interval: The recurrence interval (default 1)

        Returns:
            The next due date in YYYY-MM-DD format, or None if invalid
        """
        if not RecurrenceService.validate_pattern(pattern) or not RecurrenceService.validate_interval(interval):
            return None

        try:
            current_dt = datetime.strptime(current_due_date, "%Y-%m-%d")

            if pattern == 'daily':
                next_dt = current_dt + timedelta(days=interval)
            elif pattern == 'weekly':
                next_dt = current_dt + timedelta(weeks=interval)
            elif pattern == 'monthly':
                # Use relativedelta for proper month handling (handles month-end dates correctly)
                next_dt = current_dt + relativedelta(months=interval)
            else:
                return None

            return next_dt.strftime("%Y-%m-%d")
        except ValueError:
            return None

    @staticmethod
    def calculate_next_due_date_with_time(
        current_due_date: str,
        pattern: str,
        interval: int = 1
    ) -> Optional[str]:
        """
        Calculate the next due date with time support (YYYY-MM-DD HH:MM format).

        Args:
            current_due_date: The current due date in YYYY-MM-DD or YYYY-MM-DD HH:MM format
            pattern: The recurrence pattern ('daily', 'weekly', 'monthly')
            interval: The recurrence interval (default 1)

        Returns:
            The next due date in same format as input, or None if invalid
        """
        if not RecurrenceService.validate_pattern(pattern) or not RecurrenceService.validate_interval(interval):
            return None

        try:
            # Check if the date includes time
            has_time = " " in current_due_date or "T" in current_due_date

            if has_time:
                # Parse with time component
                if " " in current_due_date:
                    current_dt = datetime.strptime(current_due_date, "%Y-%m-%d %H:%M")
                elif "T" in current_due_date:
                    # Handle ISO format with time
                    if current_due_date.count(":") == 2:  # Includes seconds
                        current_dt = datetime.strptime(current_due_date, "%Y-%m-%dT%H:%M:%S")
                    else:
                        current_dt = datetime.strptime(current_due_date, "%Y-%m-%dT%H:%M")
                else:
                    return None
            else:
                # Parse date only
                current_dt = datetime.strptime(current_due_date, "%Y-%m-%d")

            if pattern == 'daily':
                next_dt = current_dt + timedelta(days=interval)
            elif pattern == 'weekly':
                next_dt = current_dt + timedelta(weeks=interval)
            elif pattern == 'monthly':
                # Use relativedelta for proper month handling (handles month-end dates correctly)
                next_dt = current_dt + relativedelta(months=interval)
            else:
                return None

            # Return in same format as input
            if has_time:
                if " " in current_due_date:
                    return next_dt.strftime("%Y-%m-%d %H:%M")
                elif "T" in current_due_date and current_due_date.count(":") == 2:
                    return next_dt.strftime("%Y-%m-%dT%H:%M:%S")
                else:
                    return next_dt.strftime("%Y-%m-%dT%H:%M")
            else:
                return next_dt.strftime("%Y-%m-%d")

        except ValueError:
            return None