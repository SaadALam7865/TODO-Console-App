"""
Simple test script to verify the core functionality of the Todo application
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from main import TodoApp, Task

def test_todo_app():
    print("Testing Todo Application functionality...")

    # Create a new app instance
    app = TodoApp()

    # Test 1: Add a task
    print("\n1. Testing Add Task functionality")
    task1 = app.add_task("Test Task 1", "Description for test task 1")
    print(f"   Added task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}', Completed={task1.completed}")

    # Test 2: Add another task
    task2 = app.add_task("Test Task 2", "Description for test task 2")
    print(f"   Added task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}', Completed={task2.completed}")

    # Test 3: View tasks
    print("\n2. Testing View Tasks functionality")
    tasks = app.view_tasks()
    print(f"   Total tasks: {len(tasks)}")
    for task in tasks:
        print(f"   - {task}")

    # Test 4: Update a task
    print("\n3. Testing Update Task functionality")
    updated_task = app.update_task(task1.id, "Updated Test Task 1", "Updated description")
    print(f"   Updated task: ID={updated_task.id}, Title='{updated_task.title}', Description='{updated_task.description}'")

    # Test 5: Toggle task status
    print("\n4. Testing Toggle Task Status functionality")
    toggled_task = app.toggle_task_status(task1.id)
    print(f"   Toggled task {toggled_task.id}: Status is now {'completed' if toggled_task.completed else 'incomplete'}")

    # Test 6: Delete a task
    print("\n5. Testing Delete Task functionality")
    deleted_task = app.delete_task(task2.id)
    print(f"   Deleted task: ID={deleted_task.id}, Title='{deleted_task.title}'")

    # Test 7: View tasks again to confirm deletion
    print("\n6. Testing View Tasks after deletion")
    remaining_tasks = app.view_tasks()
    print(f"   Remaining tasks: {len(remaining_tasks)}")
    for task in remaining_tasks:
        print(f"   - {task}")

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_todo_app()