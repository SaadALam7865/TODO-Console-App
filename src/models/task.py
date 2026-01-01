"""
Enhanced Task Model for Phase I - Intermediate Features

This module defines the enhanced Task class with additional fields for due dates,
priorities, tags, and creation timestamp to support intermediate features.
"""

from datetime import datetime
from typing import List, Optional


class Task:
    """Represents a single task in the todo application with enhanced fields."""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False,
                 due_date: Optional[str] = None, priority: str = "Medium",
                 tags: Optional[List[str]] = None, created_at: Optional[str] = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

        # Enhanced fields for intermediate features
        self.due_date = due_date  # Format: YYYY-MM-DD or None
        self.priority = self._validate_priority(priority)  # "High", "Medium", "Low"
        self.tags = tags if tags is not None else []  # List of tags like ["Work", "Urgent"]
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def _validate_priority(self, priority: str) -> str:
        """Validate and normalize priority value."""
        valid_priorities = {"high": "High", "medium": "Medium", "low": "Low"}
        priority_lower = priority.lower()
        if priority_lower in valid_priorities:
            return valid_priorities[priority_lower]
        return "Medium"  # Default priority

    def set_due_date(self, due_date: Optional[str]) -> None:
        """Set the due date for the task."""
        self.due_date = due_date

    def set_priority(self, priority: str) -> None:
        """Set the priority for the task."""
        self.priority = self._validate_priority(priority)

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
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            current = datetime.now()
            return due.date() < current.date()
        except ValueError:
            # If date format is invalid, consider it not overdue
            return False

    def __str__(self):
        """String representation of the task with enhanced fields."""
        status = "X" if self.completed else "O"
        overdue_indicator = " (OVERDUE)" if self.is_overdue() else ""
        due_date_str = f" | Due: {self.due_date}{overdue_indicator}" if self.due_date else ""
        priority_str = f" | Priority: {self.priority}"
        tags_str = f" | Tags: {', '.join(self.tags) if self.tags else 'None'}"

        return f"[{status}] ID: {self.id} | Title: {self.title}{due_date_str}{priority_str}{tags_str} | Description: {self.description}"