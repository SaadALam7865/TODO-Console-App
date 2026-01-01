"""
Todo Console Application
Phase I: In-Memory Python Console Application

A command-line todo manager with the following features:
1. Add Task: Create task with title, description, due date, priority, and tags
2. View Tasks: List all tasks with status indicators
3. Update Task: Modify existing task details
4. Delete Task: Remove task by unique ID
5. Mark Complete/Incomplete: Toggle task completion status
6. Add Due Date: Set due date for tasks
7. Add Priority: Set priority level for tasks
8. Add Tags: Assign tags to tasks
9. Search Tasks: Find tasks by keyword
10. Filter Tasks: Show tasks by criteria
11. Sort Tasks: Order tasks by various criteria
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
    handle_sort_tasks
)


class TodoApp:
    """Main todo application class managing tasks in memory."""

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description, due_date=None, priority="Medium", tags=None):
        """Add a new task to the application."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        # Validate due date if provided
        if due_date and not is_valid_date(due_date):
            raise ValueError(f"Invalid due date format: {due_date}. Please use YYYY-MM-DD format.")

        # Normalize priority
        normalized_priority = normalize_priority(priority)

        # Normalize tags
        normalized_tags = normalize_tags(tags) if tags else []

        task = Task(self.next_id, title.strip(), description.strip() if description else "",
                   completed=False, due_date=due_date, priority=normalized_priority, tags=normalized_tags)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def view_tasks(self):
        """Return a list of all tasks."""
        return [self.tasks[tid] for tid in sorted(self.tasks.keys())]

    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None, tags=None):
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
                raise ValueError(f"Invalid due date format: {due_date}. Please use YYYY-MM-DD format.")
            task.set_due_date(due_date)
        if priority is not None:
            task.set_priority(priority)
        if tags is not None:
            # Update tags list
            task.tags = normalize_tags(tags)

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
        task.completed = not task.completed
        return task




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
            print("\nThank you for using the Todo Console Application!")
            print("Goodbye!")
            break

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()