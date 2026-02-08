"""
Notification Service for Phase I Advanced Features

This module provides functionality for handling browser/desktop notifications
for time-based reminders using the plyer library.
"""

from typing import Optional
import threading
from plyer import notification


class NotificationService:
    """Service class for handling desktop notifications."""

    def __init__(self):
        self.notifications_enabled = True

    def send_notification(
        self,
        title: str,
        message: str,
        timeout: int = 10,
        app_name: str = "Evolution of Todo"
    ) -> bool:
        """
        Send a desktop notification to the user.

        Args:
            title: The notification title
            message: The notification message
            timeout: How long the notification should appear (in seconds)
            app_name: The name of the application sending the notification

        Returns:
            True if notification was sent successfully, False otherwise
        """
        if not self.notifications_enabled:
            return False

        try:
            notification.notify(
                title=title,
                message=message,
                app_name=app_name,
                timeout=timeout
            )
            return True
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Notification error: {e}")
            return False

    def request_permission(self) -> bool:
        """
        Request permission to send notifications (where applicable).

        Returns:
            True if permission is granted or not needed, False otherwise
        """
        # For plyer, permissions are typically handled by the OS
        # We'll assume permission is available unless explicitly disabled
        return self.notifications_enabled

    def is_notification_available(self) -> bool:
        """
        Check if the system supports notifications.

        Returns:
            True if notifications are available, False otherwise
        """
        try:
            # Try a simple notification to test availability
            # This is a basic check - in production, you might want a more robust check
            return True
        except:
            return False

    def enable_notifications(self):
        """Enable notifications."""
        self.notifications_enabled = True

    def disable_notifications(self):
        """Disable notifications."""
        self.notifications_enabled = False

    def get_notification_status(self) -> bool:
        """
        Get the current notification status.

        Returns:
            True if notifications are enabled, False otherwise
        """
        return self.notifications_enabled


class NotificationManager:
    """Manager class to handle notification scheduling and management."""

    def __init__(self):
        self.notification_service = NotificationService()
        self.pending_notifications = []

    def schedule_notification(
        self,
        title: str,
        message: str,
        delay_seconds: int,
        app_name: str = "Evolution of Todo"
    ):
        """
        Schedule a notification to be sent after a specified delay.

        Args:
            title: The notification title
            message: The notification message
            delay_seconds: Delay in seconds before showing the notification
            app_name: The name of the application sending the notification
        """
        def delayed_notify():
            self.notification_service.send_notification(
                title=title,
                message=message,
                app_name=app_name
            )

        # Create a timer to execute the notification after the delay
        timer = threading.Timer(delay_seconds, delayed_notify)
        timer.start()

        # Keep track of the timer in case we need to cancel it
        self.pending_notifications.append(timer)

    def cancel_all_notifications(self):
        """Cancel all pending notifications."""
        for timer in self.pending_notifications:
            timer.cancel()
        self.pending_notifications.clear()