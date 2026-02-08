"""
Enhanced Task Model for Phase I - Advanced Features: Intelligent Automation

This module defines the fully enhanced Task class with additional fields for due dates,
priorities, tags, creation timestamp, recurrence patterns, and reminder settings
to support advanced features.
"""

from datetime import datetime
from typing import List, Optional


class Task:
    """Represents a single task in the todo application with advanced fields."""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False,
                 due_date: Optional[str] = None, priority: str = "Medium",
                 tags: Optional[List[str]] = None, created_at: Optional[str] = None,
                 recurrence_pattern: Optional[str] = None, recurrence_interval: int = 1,
                 recurrence_end_date: Optional[str] = None, reminder_time: Optional[int] = None,
                 last_notification_sent: Optional[str] = None, is_recurring_instance: bool = False,
                 parent_task_id: Optional[int] = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

        # Enhanced fields for intermediate features
        self.due_date = due_date  # Format: YYYY-MM-DD or YYYY-MM-DD HH:MM or None
        self.priority = self._validate_priority(priority)  # "High", "Medium", "Low"
        self.tags = tags if tags is not None else []  # List of tags like ["Work", "Urgent"]
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        # Advanced fields for recurring tasks and reminders
        self.recurrence_pattern = self._validate_recurrence_pattern(recurrence_pattern)  # 'daily', 'weekly', 'monthly', None
        self.recurrence_interval = self._validate_recurrence_interval(recurrence_interval)  # Positive integer
        self.recurrence_end_date = recurrence_end_date  # Format: YYYY-MM-DD or None
        self.reminder_time = self._validate_reminder_time(reminder_time)  # Minutes before due date or None
        self.last_notification_sent = last_notification_sent  # ISO timestamp when notification was sent or None
        self.is_recurring_instance = is_recurring_instance  # True if this is a generated recurring task
        self.parent_task_id = parent_task_id  # Reference to parent task for recurring instances

    def _validate_priority(self, priority: str) -> str:
        """Validate and normalize priority value."""
        valid_priorities = {"high": "High", "medium": "Medium", "low": "Low"}
        priority_lower = priority.lower()
        if priority_lower in valid_priorities:
            return valid_priorities[priority_lower]
        return "Medium"  # Default priority

    def _validate_recurrence_pattern(self, pattern: Optional[str]) -> Optional[str]:
        """Validate and normalize recurrence pattern value."""
        if pattern is None:
            return None
        valid_patterns = {"daily": "daily", "weekly": "weekly", "monthly": "monthly",
                         "none": None, "": None}
        pattern_lower = pattern.lower()
        if pattern_lower in valid_patterns:
            return valid_patterns[pattern_lower]
        return None  # Default to no recurrence

    def _validate_recurrence_interval(self, interval: int) -> int:
        """Validate recurrence interval value."""
        if isinstance(interval, int) and interval >= 1:
            return interval
        return 1  # Default to 1

    def _validate_reminder_time(self, reminder_time: Optional[int]) -> Optional[int]:
        """Validate reminder time value."""
        if reminder_time is None:
            return None
        if isinstance(reminder_time, int) and reminder_time >= 0:
            return reminder_time
        return None  # Default to no reminder

    def set_due_date(self, due_date: Optional[str]) -> None:
        """Set the due date for the task."""
        self.due_date = due_date

    def set_priority(self, priority: str) -> None:
        """Set the priority for the task."""
        self.priority = self._validate_priority(priority)

    def set_recurrence_pattern(self, pattern: Optional[str]) -> None:
        """Set the recurrence pattern for the task."""
        self.recurrence_pattern = self._validate_recurrence_pattern(pattern)

    def set_recurrence_interval(self, interval: int) -> None:
        """Set the recurrence interval for the task."""
        self.recurrence_interval = self._validate_recurrence_interval(interval)

    def set_recurrence_end_date(self, end_date: Optional[str]) -> None:
        """Set the recurrence end date for the task."""
        self.recurrence_end_date = end_date

    def set_reminder_time(self, reminder_time: Optional[int]) -> None:
        """Set the reminder time for the task."""
        self.reminder_time = self._validate_reminder_time(reminder_time)

    def set_parent_task_id(self, parent_id: Optional[int]) -> None:
        """Set the parent task ID for recurring instances."""
        self.parent_task_id = parent_id

    def add_tag(self, tag: str) -> None:
        """Add a tag to the task if it doesn't already exist."""
        tag_capitalized = tag.capitalize()
        if tag_capitalized not in self.tags:
            self.tags.append(tag_capitalized)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the task."""
        tag_capitalized = tag.capitalize()
        if tag_capitalized in self.tags:
            self.tags.remove(tag_capitalized)

    def is_overdue(self) -> bool:
        """Check if the task is overdue based on due date and current date."""
        if not self.due_date or self.completed:
            return False

        try:
            from datetime import datetime
            # Handle both date-only and date-time formats
            if " " in self.due_date:  # Contains time
                due = datetime.strptime(self.due_date, "%Y-%m-%d %H:%M")
            elif "T" in self.due_date and self.due_date.count(":") >= 1:  # ISO format with time
                if self.due_date.count(":") == 2:  # Includes seconds
                    due = datetime.strptime(self.due_date, "%Y-%m-%dT%H:%M:%S")
                else:  # No seconds
                    due = datetime.strptime(self.due_date, "%Y-%m-%dT%H:%M")
            else:  # Date only
                due = datetime.strptime(self.due_date, "%Y-%m-%d")
            current = datetime.now()
            return due.date() < current.date()
        except ValueError:
            # If date format is invalid, consider it not overdue
            return False

    def has_upcoming_reminder(self) -> bool:
        """Check if the task has an upcoming reminder that should be triggered."""
        if self.reminder_time is None or not self.due_date or self.completed:
            return False

        try:
            from datetime import datetime, timedelta
            # Handle both date-only and date-time formats
            if " " in self.due_date:  # Contains time
                due = datetime.strptime(self.due_date, "%Y-%m-%d %H:%M")
            elif "T" in self.due_date and self.due_date.count(":") >= 1:  # ISO format with time
                if self.due_date.count(":") == 2:  # Includes seconds
                    due = datetime.strptime(self.due_date, "%Y-%m-%dT%H:%M:%S")
                else:  # No seconds
                    due = datetime.strptime(self.due_date, "%Y-%m-%dT%H:%M")
            else:  # Date only, assume due at start of day
                due_date_only = datetime.strptime(self.due_date, "%Y-%m-%d")
                due = due_date_only

            # Calculate when the reminder should be sent
            reminder_time = due - timedelta(minutes=self.reminder_time)
            current = datetime.now()

            # Check if reminder should be sent now and hasn't been sent yet
            last_sent = self.last_notification_sent
            if last_sent:
                last_sent_dt = datetime.fromisoformat(last_sent)
                return reminder_time <= current and last_sent_dt < reminder_time
            else:
                return reminder_time <= current

        except ValueError:
            # If date format is invalid, no reminder
            return False

    def is_recurring_and_not_expired(self) -> bool:
        """Check if the task is recurring and has not reached its end date."""
        if not self.recurrence_pattern:
            return False

        if not self.recurrence_end_date:
            return True  # No end date, so it's not expired

        try:
            from datetime import datetime
            end_date = datetime.strptime(self.recurrence_end_date, "%Y-%m-%d")
            current = datetime.now()
            return end_date.date() >= current.date()
        except ValueError:
            # If date format is invalid, assume it's not expired
            return True

    def __str__(self):
        """String representation of the task with advanced fields."""
        status = "X" if self.completed else "O"
        overdue_indicator = " (OVERDUE)" if self.is_overdue() else ""
        due_date_str = f" | Due: {self.due_date}{overdue_indicator}" if self.due_date else ""
        priority_str = f" | Priority: {self.priority}"
        tags_str = f" | Tags: {', '.join(self.tags) if self.tags else 'None'}"

        # Add recurrence indicator if applicable
        recurrence_indicator = ""
        if self.recurrence_pattern:
            recurrence_indicator = f" | [{self.recurrence_pattern.upper()}]"

        # Add reminder indicator if applicable
        reminder_indicator = ""
        if self.reminder_time is not None:
            reminder_indicator = f" | REM: {self.reminder_time}min"

        # Add instance indicator if it's a recurring instance
        instance_indicator = ""
        if self.is_recurring_instance:
            instance_indicator = " | [RECURRING INSTANCE]"

        return f"[{status}]{recurrence_indicator}{instance_indicator} ID: {self.id} | Title: {self.title}{due_date_str}{priority_str}{tags_str}{reminder_indicator} | Description: {self.description}"