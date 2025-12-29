"""
Todo Console Application
Phase I: In-Memory Python Console Application

A command-line todo manager with the following features:
1. Add Task: Create task with title and description
2. View Tasks: List all tasks with status indicators
3. Update Task: Modify existing task details
4. Delete Task: Remove task by unique ID
5. Mark Complete/Incomplete: Toggle task completion status
"""

class Task:
    """Represents a single task in the todo application."""

    def __init__(self, task_id, title, description, completed=False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "X" if self.completed else "O"
        return f"[{status}] ID: {self.id} | Title: {self.title} | Description: {self.description}"


class TodoApp:
    """Main todo application class managing tasks in memory."""

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description):
        """Add a new task to the application."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(self.next_id, title.strip(), description.strip() if description else "")
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def view_tasks(self):
        """Return a list of all tasks."""
        return [self.tasks[tid] for tid in sorted(self.tasks.keys())]

    def update_task(self, task_id, title=None, description=None):
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
    print("6. Exit")
    print("="*50)


def get_user_choice():
    """Get and validate user menu choice."""
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return int(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\nExiting application...")
            return 6
        except EOFError:
            print("\nExiting application...")
            return 6


def handle_add_task(app):
    """Handle the add task functionality."""
    print("\n--- ADD TASK ---")
    try:
        title = input("Enter task title: ").strip()
        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional): ").strip()

        task = app.add_task(title, description)
        print(f"Task added successfully! ID: {task.id}")
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

        # Only update if user provided new values
        new_title = title if title else None
        new_description = description if description else None

        # If user pressed Enter without typing anything, treat as no change
        if title == "":
            new_title = None
        if description == "":
            new_description = None

        updated_task = app.update_task(task_id, new_title, new_description)
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
            print("\nThank you for using the Todo Console Application!")
            print("Goodbye!")
            break

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()