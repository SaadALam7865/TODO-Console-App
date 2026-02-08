"""
Todo Console Application
Phase I: In-Memory Python Console Application

A command-line todo manager with the following features:
1. Add Task: Create task with title, description, due date, priority, and tags
2. View Tasks: List all tasks with status indicators
3. Update Task: Modify existing task details
4. Delete Task: Remove task by unique ID
5. Mark Complete/Incomplete: Toggle task completion status
6. Search Tasks: Find tasks by keyword
7. Filter Tasks: Show tasks by criteria
8. Sort Tasks: Order tasks by various criteria
9. Set/View Recurring Pattern: Configure recurring tasks
10. Set/View Reminder: Configure task reminders
11. View Upcoming Reminders: See tasks with upcoming notifications
12. Exit: Close the application
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from models.task import Task
from services.date_validator import is_valid_date
from services.priority_validator import normalize_priority
from services.tag_manager import normalize_tags
from services.search_service import search_tasks_by_keyword
from services.filter_service import filter_tasks_by_combined_criteria
from services.sort_service import (
    sort_tasks_by_due_date,
    sort_tasks_by_priority,
    sort_tasks_alphabetically,
    sort_tasks_by_creation_order,
    sort_tasks_by_completion_status
)
from services.recurrence_service import RecurrenceService
from services.notification_service import NotificationService, NotificationManager
from services.scheduler_service import SchedulerService, TaskReminderScheduler
from services.datetime_parser import DateTimeParser
from cli.menu import (
    display_menu,
    get_user_choice,
    handle_add_task,
    handle_view_tasks,
    handle_update_task,
    handle_delete_task,
    handle_toggle_status,
    handle_search_tasks,
    handle_filter_tasks,
    handle_sort_tasks,
    handle_set_recurring_pattern,
    handle_set_reminder,
    handle_view_upcoming_reminders
)


class TodoApp:
    """Main todo application class managing tasks in memory."""

    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        self.recurrence_service = RecurrenceService()
        self.notification_service = NotificationService()
        self.scheduler_service = SchedulerService()
        self.datetime_parser = DateTimeParser()
        self.task_reminder_scheduler = TaskReminderScheduler(self)
        self.notification_manager = NotificationManager()

        # Start the reminder system
        self.task_reminder_scheduler.start_reminder_system()

    def add_task(self, title, description, due_date=None, priority="Medium", tags=None,
                 recurrence_pattern=None, recurrence_interval=1, recurrence_end_date=None,
                 reminder_time=None):
        """Add a new task to the application."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        # Validate due date if provided
        if due_date and not is_valid_date(due_date):
            raise ValueError(f"Invalid due date format: {due_date}. Please use YYYY-MM-DD or YYYY-MM-DD HH:MM format.")

        # Validate recurrence pattern if provided
        if recurrence_pattern is not None and not self.recurrence_service.validate_pattern(recurrence_pattern):
            raise ValueError(f"Invalid recurrence pattern: {recurrence_pattern}. Valid patterns are: daily, weekly, monthly.")

        # Validate recurrence interval if provided
        if recurrence_interval is not None and not self.recurrence_service.validate_interval(recurrence_interval):
            raise ValueError(f"Invalid recurrence interval: {recurrence_interval}. Must be a positive integer.")

        # Validate recurrence end date if provided
        if recurrence_end_date and not self.recurrence_service.validate_end_date(recurrence_end_date, due_date):
            raise ValueError(f"Invalid recurrence end date: {recurrence_end_date}. Must be after due date in YYYY-MM-DD format.")

        # Validate reminder time if provided
        if reminder_time is not None and reminder_time < 0:
            raise ValueError(f"Invalid reminder time: {reminder_time}. Must be a positive integer representing minutes before due date.")

        # Normalize priority
        normalized_priority = normalize_priority(priority)

        # Normalize tags
        normalized_tags = normalize_tags(tags) if tags else []

        task = Task(
            self.next_id, title.strip(), description.strip() if description else "",
            completed=False, due_date=due_date, priority=normalized_priority, tags=normalized_tags,
            recurrence_pattern=recurrence_pattern, recurrence_interval=recurrence_interval,
            recurrence_end_date=recurrence_end_date, reminder_time=reminder_time
        )
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def view_tasks(self):
        """Return a list of all tasks."""
        return [self.tasks[tid] for tid in sorted(self.tasks.keys())]

    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None, tags=None,
                    recurrence_pattern=..., recurrence_interval=..., recurrence_end_date=...,
                    reminder_time=...):
        """Update an existing task."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task = self.tasks[task_id]
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        if due_date is not None:
            # Allow None to clear the due date
            if due_date and not is_valid_date(due_date):
                raise ValueError(f"Invalid due date format: {due_date}. Please use YYYY-MM-DD or YYYY-MM-DD HH:MM format.")
            task.set_due_date(due_date)
        if priority is not None:
            task.set_priority(priority)
        if tags is not None:
            # Update tags list
            task.tags = normalize_tags(tags)
        if recurrence_pattern is not ...:
            # Validate recurrence pattern
            if not self.recurrence_service.validate_pattern(recurrence_pattern):
                raise ValueError(f"Invalid recurrence pattern: {recurrence_pattern}. Valid patterns are: daily, weekly, monthly.")
            task.set_recurrence_pattern(recurrence_pattern)
        if recurrence_interval is not ...:
            # Validate recurrence interval
            if not self.recurrence_service.validate_interval(recurrence_interval):
                raise ValueError(f"Invalid recurrence interval: {recurrence_interval}. Must be a positive integer.")
            task.set_recurrence_interval(recurrence_interval)
        if recurrence_end_date is not ...:
            # Validate recurrence end date
            if not self.recurrence_service.validate_end_date(recurrence_end_date, task.due_date):
                raise ValueError(f"Invalid recurrence end date: {recurrence_end_date}. Must be after due date in YYYY-MM-DD format.")
            task.set_recurrence_end_date(recurrence_end_date)
        if reminder_time is not ...:
            # Validate reminder time
            if reminder_time is not None and reminder_time < 0:
                raise ValueError(f"Invalid reminder time: {reminder_time}. Must be a positive integer representing minutes before due date.")
            task.set_reminder_time(reminder_time)

        return task

    def delete_task(self, task_id):
        """Delete a task by ID."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")

        deleted_task = self.tasks.pop(task_id)
        return deleted_task

    def toggle_task_status(self, task_id):
        """Toggle the completion status of a task."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task = self.tasks[task_id]
        original_completed_status = task.completed
        task.completed = not task.completed

        # Check if the task was just marked as complete and has recurrence
        if task.completed and not original_completed_status and task.recurrence_pattern:
            # Create a new recurring instance if the task is recurring and not expired
            if task.is_recurring_and_not_expired():
                self._create_recurring_task_instance(task)

        return task

    def _create_recurring_task_instance(self, completed_task):
        """Create a new task instance for a recurring task that was just completed."""
        # Calculate the next due date based on the recurrence pattern
        if completed_task.due_date:
            next_due_date = self.recurrence_service.calculate_next_due_date_with_time(
                completed_task.due_date,
                completed_task.recurrence_pattern,
                completed_task.recurrence_interval
            )
        else:
            next_due_date = None

        # Only create the new instance if the next due date is valid and not past the end date
        if next_due_date:
            # Check if the next due date is after the recurrence end date (if specified)
            if completed_task.recurrence_end_date:
                from datetime import datetime
                try:
                    next_dt = datetime.strptime(next_due_date.split()[0] if ' ' in next_due_date else next_due_date, "%Y-%m-%d")
                    end_dt = datetime.strptime(completed_task.recurrence_end_date, "%Y-%m-%d")
                    if next_dt.date() > end_dt.date():
                        # Don't create a new instance if it would exceed the end date
                        return
                except ValueError:
                    # If date parsing fails, continue with creation
                    pass

            # Create a new task with the same properties but updated due date
            new_task = Task(
                self.next_id,
                completed_task.title,
                completed_task.description,
                completed=False,  # New instance starts as incomplete
                due_date=next_due_date,
                priority=completed_task.priority,
                tags=completed_task.tags.copy(),  # Copy the tags
                recurrence_pattern=completed_task.recurrence_pattern,
                recurrence_interval=completed_task.recurrence_interval,
                recurrence_end_date=completed_task.recurrence_end_date,
                reminder_time=completed_task.reminder_time,
                is_recurring_instance=True,  # Mark as a recurring instance
                parent_task_id=completed_task.id  # Reference to the parent task
            )

            self.tasks[self.next_id] = new_task
            self.next_id += 1




def main():
    """Main application loop."""
    print("Welcome to the Todo Console Application!")
    print("This is Phase I: In-Memory Python Console Application")

    app = TodoApp()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_add_task(app)
        elif choice == 2:
            handle_view_tasks(app)
        elif choice == 3:
            handle_update_task(app)
        elif choice == 4:
            handle_delete_task(app)
        elif choice == 5:
            handle_toggle_status(app)
        elif choice == 6:
            handle_search_tasks(app)
        elif choice == 7:
            handle_filter_tasks(app)
        elif choice == 8:
            handle_sort_tasks(app)
        elif choice == 9:
            handle_set_recurring_pattern(app)
        elif choice == 10:
            handle_set_reminder(app)
        elif choice == 11:
            handle_view_upcoming_reminders(app)
        elif choice == 12:
            print("\nThank you for using the Todo Console Application!")
            print("Goodbye!")
            break

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()