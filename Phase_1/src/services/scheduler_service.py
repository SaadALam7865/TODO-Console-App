"""
Scheduler Service for Phase I Advanced Features

This module provides functionality for scheduling background tasks,
particularly for checking upcoming reminders and recurring tasks.
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timedelta
import atexit
from typing import Callable, Any, Optional
import threading


class SchedulerService:
    """Service class for handling background scheduling of tasks."""

    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler_started = False
        self.check_interval = 60  # Check every 60 seconds by default
        self.check_functions = []

    def start_scheduler(self):
        """Start the background scheduler."""
        if not self.scheduler_started:
            # Add a default job that runs at the specified interval
            self.scheduler.add_job(
                func=self._run_check_functions,
                trigger=IntervalTrigger(seconds=self.check_interval),
                id='reminder_check_job',
                name='Check for upcoming reminders and recurring tasks',
                replace_existing=True
            )

            self.scheduler.start()
            self.scheduler_started = True

            # Shut down the scheduler when exiting the app
            atexit.register(self.shutdown)

    def stop_scheduler(self):
        """Stop the background scheduler."""
        if self.scheduler_started:
            self.scheduler.shutdown()
            self.scheduler_started = False

    def shutdown(self):
        """Graceful shutdown of the scheduler."""
        if self.scheduler_started:
            self.scheduler.shutdown(wait=True)
            self.scheduler_started = False

    def add_check_function(self, func: Callable, interval: int = 60):
        """
        Add a function to be called at regular intervals.

        Args:
            func: The function to call
            interval: Interval in seconds between calls
        """
        self.check_functions.append({
            'function': func,
            'interval': interval
        })

    def _run_check_functions(self):
        """Internal method to run all registered check functions."""
        for check_info in self.check_functions:
            try:
                check_info['function']()
            except Exception as e:
                print(f"Error in scheduled function: {e}")

    def schedule_task(
        self,
        func: Callable,
        run_time: datetime,
        id: Optional[str] = None,
        name: Optional[str] = None
    ):
        """
        Schedule a single task to run at a specific time.

        Args:
            func: The function to call
            run_time: When to run the function
            id: Optional ID for the job
            name: Optional name for the job
        """
        self.scheduler.add_job(
            func=func,
            trigger='date',
            run_date=run_time,
            id=id,
            name=name
        )

    def schedule_recurring_task(
        self,
        func: Callable,
        interval_seconds: int,
        id: Optional[str] = None,
        name: Optional[str] = None
    ):
        """
        Schedule a recurring task to run at specified intervals.

        Args:
            func: The function to call
            interval_seconds: Interval in seconds between runs
            id: Optional ID for the job
            name: Optional name for the job
        """
        trigger = IntervalTrigger(seconds=interval_seconds)
        self.scheduler.add_job(
            func=func,
            trigger=trigger,
            id=id,
            name=name
        )

    def get_jobs(self):
        """Get a list of all scheduled jobs."""
        return self.scheduler.get_jobs()

    def remove_job(self, job_id: str):
        """
        Remove a scheduled job by ID.

        Args:
            job_id: The ID of the job to remove
        """
        self.scheduler.remove_job(job_id)

    def update_check_interval(self, new_interval: int):
        """
        Update the interval for checking reminders.

        Args:
            new_interval: New interval in seconds
        """
        self.check_interval = new_interval
        # Restart the scheduler to apply the new interval
        if self.scheduler_started:
            self.scheduler.remove_job('reminder_check_job')
            self.scheduler.add_job(
                func=self._run_check_functions,
                trigger=IntervalTrigger(seconds=self.check_interval),
                id='reminder_check_job',
                name='Check for upcoming reminders and recurring tasks',
                replace_existing=True
            )


class TaskReminderScheduler:
    """Specialized scheduler for handling task reminders."""

    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.scheduler_service = SchedulerService()

    def start_reminder_system(self):
        """Start the reminder checking system."""
        # Add the reminder check function
        self.scheduler_service.add_check_function(
            self.check_for_upcoming_reminders,
            interval=60  # Check every minute
        )

        # Start the scheduler
        self.scheduler_service.start_scheduler()

    def stop_reminder_system(self):
        """Stop the reminder checking system."""
        self.scheduler_service.stop_scheduler()

    def check_for_upcoming_reminders(self):
        """Check for tasks with upcoming reminders and send notifications."""
        if not self.task_manager:
            return

        current_time = datetime.now()

        # Get all tasks that have reminders set
        for task in self.task_manager.tasks.values():
            if hasattr(task, 'reminder_time') and task.reminder_time is not None:
                if hasattr(task, 'due_date') and task.due_date:
                    try:
                        # Parse the due date - handle both date-only and datetime formats
                        if ' ' in task.due_date:  # Contains time
                            due_time = datetime.strptime(task.due_date, "%Y-%m-%d %H:%M")
                        elif 'T' in task.due_date and task.due_date.count(':') >= 1:  # ISO format with time
                            if task.due_date.count(':') == 2:  # Includes seconds
                                due_time = datetime.strptime(task.due_date, "%Y-%m-%dT%H:%M:%S")
                            else:  # No seconds
                                due_time = datetime.strptime(task.due_date, "%Y-%m-%dT%H:%M")
                        else:  # Date only, assume due at start of day
                            due_date_only = datetime.strptime(task.due_date, "%Y-%m-%d")
                            due_time = due_date_only

                        # Calculate when the reminder should be sent
                        reminder_time = due_time - timedelta(minutes=task.reminder_time)

                        # Check if we should send the reminder now
                        # Only send if reminder time is now or was missed, and hasn't been sent yet
                        last_sent = getattr(task, 'last_notification_sent', None)

                        should_send = (
                            reminder_time <= current_time and
                            (last_sent is None or datetime.fromisoformat(last_sent) < reminder_time)
                        )

                        if should_send:
                            # Send notification using the task manager's notification service
                            # The task_manager should have a reference to the notification service
                            if hasattr(self.task_manager, 'notification_manager'):
                                notification_service = self.task_manager.notification_manager.notification_service
                            elif hasattr(self.task_manager, 'notification_service'):
                                notification_service = self.task_manager.notification_service
                            else:
                                # Fallback: create a new notification service
                                from .notification_service import NotificationService
                                notification_service = NotificationService()

                            title = f"Task Reminder: {task.title}"
                            message = f"Task '{task.title}' is due soon (at {task.due_date})"

                            notification_service.send_notification(
                                title=title,
                                message=message
                            )

                            # Update the task to record that notification was sent
                            task.last_notification_sent = current_time.isoformat()

                    except ValueError:
                        # If date parsing fails, skip this task
                        continue

    def schedule_recurring_tasks_check(self):
        """Schedule checking for recurring tasks that need to generate new instances."""
        self.scheduler_service.add_check_function(
            self.check_for_completed_recurring_tasks,
            interval=30  # Check every 30 seconds for completed recurring tasks
        )

    def check_for_completed_recurring_tasks(self):
        """Check for completed recurring tasks and generate new instances."""
        if not self.task_manager:
            return

        current_time = datetime.now()

        # Get all completed recurring tasks
        for task in self.task_manager.tasks.values():
            if (hasattr(task, 'recurrence_pattern') and
                task.recurrence_pattern and
                task.completed and
                hasattr(task, 'is_recurring_instance') and
                not task.is_recurring_instance):

                # Check if we need to create a new instance based on recurrence
                # This would typically be handled when the task is marked complete
                # But we'll do a periodic check to ensure no missed instances
                pass  # Actual implementation would be in the task completion logic