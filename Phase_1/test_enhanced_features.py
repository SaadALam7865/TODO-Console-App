"""
Test script for the enhanced todo application
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.task import Task
from services.date_validator import is_valid_date
from services.priority_validator import normalize_priority
from services.tag_manager import normalize_tags
from services.search_service import search_tasks_by_keyword
from services.filter_service import filter_tasks_by_status
from services.sort_service import sort_tasks_by_priority

def test_enhanced_task():
    print("Testing enhanced Task model...")

    # Create a task with all enhanced features
    task = Task(
        task_id=1,
        title="Test Task",
        description="This is a test task with enhanced features",
        completed=False,
        due_date="2026-12-31",
        priority="High",
        tags=["Work", "Urgent"]
    )

    print(f"Task created: {task}")
    print(f"Task ID: {task.id}")
    print(f"Task Title: {task.title}")
    print(f"Task Description: {task.description}")
    print(f"Task Completed: {task.completed}")
    print(f"Task Due Date: {task.due_date}")
    print(f"Task Priority: {task.priority}")
    print(f"Task Tags: {task.tags}")
    print(f"Task Created At: {task.created_at}")
    print(f"Is Overdue: {task.is_overdue()}")
    print()

def test_date_validation():
    print("Testing date validation...")

    # Test valid date
    print(f"Valid date '2026-12-31': {is_valid_date('2026-12-31')}")

    # Test invalid date format
    print(f"Invalid format '12/31/2026': {is_valid_date('12/31/2026')}")

    # Test invalid date
    print(f"Invalid date '2026-02-30': {is_valid_date('2026-02-30')}")

    # Test valid date
    print(f"Valid date '2026-02-28': {is_valid_date('2026-02-28')}")
    print()

def test_priority_validation():
    print("Testing priority validation...")

    print(f"Normalize 'high': {normalize_priority('high')}")
    print(f"Normalize 'HIGH': {normalize_priority('HIGH')}")
    print(f"Normalize 'Medium': {normalize_priority('Medium')}")
    print(f"Normalize 'low': {normalize_priority('low')}")
    print(f"Invalid priority 'invalid': {normalize_priority('invalid')}")
    print()

def test_tag_management():
    print("Testing tag management...")

    print(f"Normalize tags ['work', 'personal']: {normalize_tags(['work', 'personal'])}")
    print(f"Add tag 'work' to ['Home']: {normalize_tags(['Home']) + ['Work']}")
    print()

def test_services():
    print("Testing services...")

    # Create some test tasks
    task1 = Task(1, "Urgent Work Task", "This is an urgent work task", False, "2024-01-01", "High", ["Work"])
    task2 = Task(2, "Personal Project", "Working on a personal project", False, "2026-12-31", "Medium", ["Personal"])
    task3 = Task(3, "Low Priority Task", "This is a low priority task", True, None, "Low", ["Home"])

    tasks = [task1, task2, task3]

    # Test search service
    search_results = search_tasks_by_keyword(tasks, "work")
    print(f"Search for 'work' found {len(search_results)} tasks")

    # Test filter service
    completed_tasks = filter_tasks_by_status(tasks, True)
    print(f"Filter for completed tasks found {len(completed_tasks)} tasks")

    # Test sort service
    sorted_tasks = sort_tasks_by_priority(tasks, ascending=False)  # High to Low
    print(f"Tasks sorted by priority (High to Low): {[task.priority for task in sorted_tasks]}")
    print()

if __name__ == "__main__":
    print("Running tests for enhanced todo application...")
    print()

    test_enhanced_task()
    test_date_validation()
    test_priority_validation()
    test_tag_management()
    test_services()

    print("All tests completed successfully!")