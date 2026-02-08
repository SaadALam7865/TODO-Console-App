"""
Enhanced CLI Menu for Phase I - Intermediate Features

This module provides the CLI menu system with all functionality for the enhanced todo app.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.task import Task
from services.date_validator import is_valid_date
from services.priority_validator import normalize_priority
from services.tag_manager import normalize_tags


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("TODO APPLICATION - MAIN MENU")
    print("="*50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Sort Tasks")
    print("9. Set/View Recurring Pattern")
    print("10. Set/View Reminder")
    print("11. View Upcoming Reminders")
    print("12. Exit")
    print("="*50)


def get_user_choice():
    """Get and validate user menu choice."""
    while True:
        try:
            choice = input("Enter your choice (1-12): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
                return int(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 12.")
        except KeyboardInterrupt:
            print("\nExiting application...")
            return 12  # Exit option
        except EOFError:
            print("\nExiting application...")
            return 12  # Exit option


def handle_add_task(app):
    """Handle the add task functionality."""
    print("\n--- ADD TASK ---")
    try:
        title = input("Enter task title: ").strip()
        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional): ").strip()

        # Get due date (optional)
        due_date = input("Enter due date (YYYY-MM-DD or YYYY-MM-DD HH:MM format, optional): ").strip()
        if not due_date:
            due_date = None

        # Get priority (optional, default to Medium)
        priority = input("Enter priority (High/Medium/Low, default: Medium): ").strip()
        if not priority:
            priority = "Medium"

        # Get tags (optional, comma-separated)
        tags_input = input("Enter tags (comma-separated, e.g., Work,Personal, optional): ").strip()
        tags = []
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        # Get recurrence pattern (optional)
        recurrence_pattern = input("Enter recurrence pattern (daily/weekly/monthly, optional): ").strip()
        if not recurrence_pattern:
            recurrence_pattern = None

        # Get recurrence interval (optional, default to 1)
        recurrence_interval_input = input("Enter recurrence interval (number of days/weeks/months, default: 1): ").strip()
        if recurrence_interval_input:
            try:
                recurrence_interval = int(recurrence_interval_input)
            except ValueError:
                print("Invalid interval. Using default value 1.")
                recurrence_interval = 1
        else:
            recurrence_interval = 1

        # Get recurrence end date (optional)
        recurrence_end_date = input("Enter recurrence end date (YYYY-MM-DD, optional): ").strip()
        if not recurrence_end_date:
            recurrence_end_date = None

        # Get reminder time (optional)
        reminder_time_input = input("Enter reminder time in minutes before due date (optional): ").strip()
        if reminder_time_input:
            try:
                reminder_time = int(reminder_time_input)
            except ValueError:
                print("Invalid reminder time. No reminder will be set.")
                reminder_time = None
        else:
            reminder_time = None

        task = app.add_task(
            title, description, due_date, priority, tags,
            recurrence_pattern, recurrence_interval, recurrence_end_date, reminder_time
        )
        print(f"Task added successfully! ID: {task.id}")
        if task.recurrence_pattern:
            print(f"Recurring task: {task.recurrence_pattern} every {task.recurrence_interval} {'day' if task.recurrence_pattern == 'daily' else 'week' if task.recurrence_pattern == 'weekly' else 'month'}{'s' if task.recurrence_interval != 1 else ''}")
        if task.reminder_time is not None:
            print(f"Reminder set: {task.reminder_time} minutes before due date")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_view_tasks(app):
    """Handle the view tasks functionality."""
    print("\n--- VIEW TASKS ---")
    tasks = app.view_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print(f"Total tasks: {len(tasks)}")
    for task in tasks:
        print(task)


def handle_update_task(app):
    """Handle the update task functionality."""
    print("\n--- UPDATE TASK ---")
    try:
        if not app.tasks:
            print("No tasks available to update.")
            return

        task_id = int(input("Enter task ID to update: "))

        # Check if task exists and display current details
        if task_id not in app.tasks:
            print(f"Task with ID {task_id} does not exist.")
            return

        current_task = app.tasks[task_id]
        print(f"Current task: {current_task}")

        title = input(f"Enter new title (current: '{current_task.title}', press Enter to keep current): ").strip()
        description = input(f"Enter new description (current: '{current_task.description}', press Enter to keep current): ").strip()

        # Get new due date (optional)
        due_date = input(f"Enter new due date (current: '{current_task.due_date}', YYYY-MM-DD or YYYY-MM-DD HH:MM format, press Enter to keep current): ").strip()

        # Get new priority (optional)
        priority = input(f"Enter new priority (current: '{current_task.priority}', High/Medium/Low, press Enter to keep current): ").strip()

        # Get new tags (optional)
        tags_input = input(f"Enter new tags (current: '{', '.join(current_task.tags) if current_task.tags else 'None'}', comma-separated, press Enter to keep current): ").strip()

        # Get new recurrence pattern (optional)
        recurrence_pattern = input(f"Enter new recurrence pattern (current: '{current_task.recurrence_pattern}', daily/weekly/monthly, press Enter to keep current): ").strip()

        # Get new recurrence interval (optional)
        recurrence_interval_input = input(f"Enter new recurrence interval (current: '{current_task.recurrence_interval}', press Enter to keep current): ").strip()

        # Get new recurrence end date (optional)
        recurrence_end_date = input(f"Enter new recurrence end date (current: '{current_task.recurrence_end_date}', YYYY-MM-DD, press Enter to keep current): ").strip()

        # Get new reminder time (optional)
        reminder_time_input = input(f"Enter new reminder time in minutes before due date (current: '{current_task.reminder_time}', press Enter to keep current): ").strip()

        # Only update if user provided new values
        new_title = title if title else None
        new_description = description if description else None
        new_due_date = due_date if due_date else None
        new_priority = priority if priority else None
        new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else None
        new_recurrence_pattern = recurrence_pattern if recurrence_pattern else None
        new_recurrence_end_date = recurrence_end_date if recurrence_end_date else None

        # Handle numeric inputs
        if recurrence_interval_input:
            try:
                new_recurrence_interval = int(recurrence_interval_input)
            except ValueError:
                print("Invalid interval. Keeping current value.")
                new_recurrence_interval = None
        else:
            new_recurrence_interval = None

        if reminder_time_input:
            try:
                new_reminder_time = int(reminder_time_input)
            except ValueError:
                print("Invalid reminder time. Keeping current value.")
                new_reminder_time = None
        else:
            new_reminder_time = None

        # If user pressed Enter without typing anything, treat as no change
        if title == "":
            new_title = None
        if description == "":
            new_description = None
        if due_date == "":
            new_due_date = None
        if priority == "":
            new_priority = None
        if tags_input == "":
            new_tags = None
        if recurrence_pattern == "":
            new_recurrence_pattern = None  # This will clear the recurrence pattern
        if recurrence_end_date == "":
            new_recurrence_end_date = None  # This will clear the recurrence end date
        if reminder_time_input == "":
            new_reminder_time = None

        updated_task = app.update_task(
            task_id, new_title, new_description, new_due_date, new_priority, new_tags,
            new_recurrence_pattern, new_recurrence_interval, new_recurrence_end_date,
            new_reminder_time
        )
        print(f"Task updated successfully!")
        print(f"Updated task: {updated_task}")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid task ID (number).")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_delete_task(app):
    """Handle the delete task functionality."""
    print("\n--- DELETE TASK ---")
    try:
        if not app.tasks:
            print("No tasks available to delete.")
            return

        task_id = int(input("Enter task ID to delete: "))

        deleted_task = app.delete_task(task_id)
        print(f"Task deleted successfully!")
        print(f"Deleted task: {deleted_task}")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid task ID (number).")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_toggle_status(app):
    """Handle the toggle task status functionality."""
    print("\n--- TOGGLE TASK STATUS ---")
    try:
        if not app.tasks:
            print("No tasks available to toggle.")
            return

        task_id = int(input("Enter task ID to toggle status: "))

        if task_id not in app.tasks:
            print(f"Task with ID {task_id} does not exist.")
            return

        task = app.toggle_task_status(task_id)
        status = "completed" if task.completed else "incomplete"
        print(f"Task status updated successfully! Task is now {status}.")
        print(f"Updated task: {task}")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid task ID (number).")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_search_tasks(app):
    """Handle the search tasks functionality."""
    print("\n--- SEARCH TASKS ---")
    try:
        if not app.tasks:
            print("No tasks available to search.")
            return

        keyword = input("Enter keyword to search (in title or description): ").strip()
        if not keyword:
            print("No keyword provided. Please enter a keyword to search.")
            return

        # Use search service to find matching tasks
        all_tasks = list(app.tasks.values())
        from src.services.search_service import search_tasks_by_keyword
        matching_tasks = search_tasks_by_keyword(all_tasks, keyword)

        if not matching_tasks:
            print(f"No tasks found matching '{keyword}'.")
            return

        print(f"Found {len(matching_tasks)} task(s) matching '{keyword}':")
        for task in sorted(matching_tasks, key=lambda t: t.id):
            print(task)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_filter_tasks(app):
    """Handle the filter tasks functionality."""
    print("\n--- FILTER TASKS ---")
    try:
        if not app.tasks:
            print("No tasks available to filter.")
            return

        print("Filter options:")
        print("1. Filter by completion status")
        print("2. Filter by priority")
        print("3. Filter by tag")
        print("4. Filter by due date status")
        print("5. Back to main menu")

        filter_choice = input("Select filter option (1-5): ").strip()

        filtered_tasks = list(app.tasks.values())

        if filter_choice == '1':
            # Filter by completion status
            status_choice = input("Show (1) Complete tasks, (2) Incomplete tasks, (3) All tasks: ").strip()
            if status_choice == '1':
                filtered_tasks = [task for task in filtered_tasks if task.completed]
            elif status_choice == '2':
                filtered_tasks = [task for task in filtered_tasks if not task.completed]
            elif status_choice == '3':
                pass  # Show all tasks
            else:
                print("Invalid choice. Showing all tasks.")
        elif filter_choice == '2':
            # Filter by priority
            priority_choice = input("Enter priority to filter by (High/Medium/Low): ").strip()
            if priority_choice.lower() in ['high', 'medium', 'low']:
                from src.services.priority_validator import normalize_priority
                normalized_priority = normalize_priority(priority_choice)
                filtered_tasks = [task for task in filtered_tasks if task.priority == normalized_priority]
            else:
                print("Invalid priority. Please enter High, Medium, or Low.")
                return
        elif filter_choice == '3':
            # Filter by tag
            tag_choice = input("Enter tag to filter by (Work/Home/Personal): ").strip()
            if tag_choice.lower() in ['work', 'home', 'personal']:
                from src.services.tag_manager import normalize_tag
                normalized_tag = normalize_tag(tag_choice)
                filtered_tasks = [task for task in filtered_tasks if normalized_tag in task.tags]
            else:
                print("Invalid tag. Please enter Work, Home, or Personal.")
                return
        elif filter_choice == '4':
            # Filter by due date status
            date_choice = input("Show (1) Overdue tasks, (2) Tasks with due date, (3) Tasks without due date: ").strip()
            if date_choice == '1':
                filtered_tasks = [task for task in filtered_tasks if task.is_overdue()]
            elif date_choice == '2':
                filtered_tasks = [task for task in filtered_tasks if task.due_date is not None]
            elif date_choice == '3':
                filtered_tasks = [task for task in filtered_tasks if task.due_date is None]
            else:
                print("Invalid choice. Showing all tasks.")
        elif filter_choice == '5':
            print("Returning to main menu.")
            return
        else:
            print("Invalid choice. Showing all tasks.")
            return

        if not filtered_tasks:
            print("No tasks match the selected filter criteria.")
            return

        print(f"Filtered tasks ({len(filtered_tasks)} found):")
        for task in sorted(filtered_tasks, key=lambda t: t.id):
            print(task)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_sort_tasks(app):
    """Handle the sort tasks functionality."""
    print("\n--- SORT TASKS ---")
    try:
        if not app.tasks:
            print("No tasks available to sort.")
            return

        print("Sort options:")
        print("1. Sort by due date")
        print("2. Sort by priority")
        print("3. Sort alphabetically by title")
        print("4. Sort by creation order")
        print("5. Sort by completion status")
        print("6. Back to main menu")

        sort_choice = input("Select sort option (1-6): ").strip()

        tasks_to_sort = list(app.tasks.values())

        if sort_choice == '1':
            # Sort by due date
            order_choice = input("Sort order (1) Ascending, (2) Descending: ").strip()
            ascending = order_choice != '2'
            from src.services.sort_service import sort_tasks_by_due_date
            tasks_to_sort = sort_tasks_by_due_date(tasks_to_sort, ascending)
        elif sort_choice == '2':
            # Sort by priority
            order_choice = input("Sort order (1) Ascending (Low to High), (2) Descending (High to Low): ").strip()
            ascending = order_choice != '2'
            from src.services.sort_service import sort_tasks_by_priority
            tasks_to_sort = sort_tasks_by_priority(tasks_to_sort, ascending)
        elif sort_choice == '3':
            # Sort alphabetically by title
            order_choice = input("Sort order (1) Ascending (A to Z), (2) Descending (Z to A): ").strip()
            ascending = order_choice != '2'
            from src.services.sort_service import sort_tasks_alphabetically
            tasks_to_sort = sort_tasks_alphabetically(tasks_to_sort, ascending)
        elif sort_choice == '4':
            # Sort by creation order (ID)
            order_choice = input("Sort order (1) Ascending (oldest first), (2) Descending (newest first): ").strip()
            ascending = order_choice != '2'
            from src.services.sort_service import sort_tasks_by_creation_order
            tasks_to_sort = sort_tasks_by_creation_order(tasks_to_sort, ascending)
        elif sort_choice == '5':
            # Sort by completion status
            order_choice = input("Sort order (1) Incomplete first, (2) Complete first: ").strip()
            incomplete_first = order_choice != '2'
            from src.services.sort_service import sort_tasks_by_completion_status
            tasks_to_sort = sort_tasks_by_completion_status(tasks_to_sort, incomplete_first)
        elif sort_choice == '6':
            print("Returning to main menu.")
            return
        else:
            print("Invalid choice. Showing unsorted tasks.")
            return

        print(f"Sorted tasks ({len(tasks_to_sort)} total):")
        for task in tasks_to_sort:
            print(task)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_set_recurring_pattern(app):
    """Handle setting recurring pattern for a task."""
    print("\n--- SET/VIEW RECURRING PATTERN ---")
    try:
        if not app.tasks:
            print("No tasks available.")
            return

        print("Current tasks:")
        for task in app.tasks.values():
            print(task)

        task_id = int(input("Enter task ID to set/view recurring pattern: "))
        if task_id not in app.tasks:
            print(f"Task with ID {task_id} does not exist.")
            return

        task = app.tasks[task_id]
        print(f"Current task: {task}")

        # Show current recurrence settings
        if task.recurrence_pattern:
            print(f"Current recurrence: {task.recurrence_pattern} every {task.recurrence_interval} {'day' if task.recurrence_pattern == 'daily' else 'week' if task.recurrence_pattern == 'weekly' else 'month'}{'s' if task.recurrence_interval != 1 else ''}")
            if task.recurrence_end_date:
                print(f"End date: {task.recurrence_end_date}")
        else:
            print("Task currently has no recurrence pattern.")

        # Ask if user wants to update or clear
        action = input("Enter 'set' to set recurrence, 'clear' to remove, or 'view' to just view: ").strip().lower()

        if action == 'clear':
            app.update_task(task_id, recurrence_pattern=None, recurrence_interval=1, recurrence_end_date=None)
            print("Recurring pattern cleared successfully.")
        elif action == 'set':
            # Get new recurrence pattern
            pattern = input("Enter recurrence pattern (daily/weekly/monthly, or press Enter to keep current): ").strip()
            if pattern == "":
                pattern = task.recurrence_pattern  # Keep current if empty

            # Get new recurrence interval
            interval_input = input("Enter recurrence interval (number of days/weeks/months, or press Enter to keep current): ").strip()
            if interval_input:
                try:
                    interval = int(interval_input)
                except ValueError:
                    print("Invalid interval. Keeping current value.")
                    interval = task.recurrence_interval
            else:
                interval = task.recurrence_interval  # Keep current if empty

            # Get new recurrence end date
            end_date = input("Enter recurrence end date (YYYY-MM-DD, or press Enter to keep current): ").strip()
            if end_date == "":
                end_date = task.recurrence_end_date  # Keep current if empty

            # Update the task with new recurrence settings
            app.update_task(task_id, recurrence_pattern=pattern, recurrence_interval=interval, recurrence_end_date=end_date)
            print("Recurring pattern updated successfully.")
        elif action == 'view':
            print("Current recurrence settings displayed above.")
        else:
            print("Invalid action. Use 'set', 'clear', or 'view'.")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid task ID (number).")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_set_reminder(app):
    """Handle setting reminder for a task."""
    print("\n--- SET/VIEW REMINDER ---")
    try:
        if not app.tasks:
            print("No tasks available.")
            return

        print("Current tasks:")
        for task in app.tasks.values():
            print(task)

        task_id = int(input("Enter task ID to set/view reminder: "))
        if task_id not in app.tasks:
            print(f"Task with ID {task_id} does not exist.")
            return

        task = app.tasks[task_id]
        print(f"Current task: {task}")

        # Show current reminder settings
        if task.reminder_time is not None:
            print(f"Current reminder: {task.reminder_time} minutes before due date")
        else:
            print("Task currently has no reminder set.")

        # Ask if user wants to update or clear
        action = input("Enter 'set' to set reminder, 'clear' to remove, or 'view' to just view: ").strip().lower()

        if action == 'clear':
            app.update_task(task_id, reminder_time=None)
            print("Reminder cleared successfully.")
        elif action == 'set':
            # Get new reminder time
            reminder_input = input("Enter reminder time in minutes before due date (or press Enter to keep current): ").strip()
            if reminder_input:
                try:
                    reminder_time = int(reminder_input)
                    if reminder_time < 0:
                        print("Invalid reminder time. No reminder will be set.")
                        return
                except ValueError:
                    print("Invalid reminder time. No reminder will be set.")
                    return
            else:
                reminder_time = task.reminder_time  # Keep current if empty

            # Update the task with new reminder settings
            app.update_task(task_id, reminder_time=reminder_time)
            print("Reminder updated successfully.")
        elif action == 'view':
            print("Current reminder settings displayed above.")
        else:
            print("Invalid action. Use 'set', 'clear', or 'view'.")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid task ID (number).")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_view_upcoming_reminders(app):
    """Handle viewing upcoming reminders."""
    print("\n--- VIEW UPCOMING REMINDERS ---")
    try:
        if not app.tasks:
            print("No tasks available.")
            return

        # Find tasks with upcoming reminders
        upcoming_reminders = []
        for task in app.tasks.values():
            if task.has_upcoming_reminder():
                upcoming_reminders.append(task)

        if not upcoming_reminders:
            print("No upcoming reminders found.")
            return

        print(f"Found {len(upcoming_reminders)} task(s) with upcoming reminders:")
        for task in sorted(upcoming_reminders, key=lambda t: t.id):
            print(task)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")