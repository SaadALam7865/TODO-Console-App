# Spec 15: Time Reminders & Browser Notifications

## Feature Overview
Enable users to set specific times for reminders before due dates and deliver browser notifications at those times. The system will include a background scheduler to check for upcoming due dates and trigger browser notifications to alert users.

## User Scenarios & Testing

### Primary User Scenarios
1. **Set reminder time**: User specifies how long before a due date they want to receive a notification (e.g., 1 hour, 1 day)
2. **Receive browser notification**: System displays browser notification at the specified reminder time
3. **Manage notification settings**: User can enable/disable notifications or adjust reminder timing
4. **Background scheduling**: System runs background checks to identify upcoming reminders without blocking console operations
5. **Handle notification permissions**: System requests appropriate permissions and handles cases where notifications are blocked

### Acceptance Scenarios
1. When a task has a reminder set, the system displays a browser notification at the specified time before due date
2. Users can set different reminder times (e.g., 30 minutes, 1 hour, 1 day before due)
3. Background scheduler runs without interfering with console operations
4. System handles notification permission denial gracefully
5. Users can disable notifications without losing other functionality

## Functional Requirements

### Core Functionality
1. **Reminder Time Setting**: System shall allow users to specify reminder offset times (in minutes before due date) when creating or updating tasks
2. **Background Scheduler**: System shall run a background process to check for upcoming reminders at regular intervals
3. **Browser Notification Delivery**: System shall display browser notifications when reminder time is reached
4. **Notification Permission Handling**: System shall request and handle browser notification permissions appropriately
5. **Reminder Management**: System shall allow users to enable/disable reminders for individual tasks

### Data Requirements
6. **Extended Task Model**: System shall extend the Task model with reminder-related fields:
   - reminder_time: integer representing minutes before due date (e.g., 60 for 1 hour before)
   - last_notification_sent: timestamp tracking when last notification was sent
   - notifications_enabled: boolean to enable/disable notifications for this task

### User Interface Requirements
7. **Task Creation Enhancement**: System shall add reminder time option to the task creation interface
8. **Task Update Enhancement**: System shall allow modification of reminder settings in the task update interface
9. **Task List Display**: System shall show reminder status in the task list view
10. **Notification Settings**: System shall provide global settings to enable/disable notifications

### Notification System Requirements
11. **Cross-Browser Compatibility**: System shall work with major browsers (Chrome, Firefox, Edge) using standard notification APIs
12. **Time Zone Handling**: System shall use system local time for all time calculations
13. **Time Format Support**: System shall accept flexible time formats (YYYY-MM-DD HH:MM) for due dates with time
14. **Background Process**: System shall implement non-blocking background scheduler that doesn't interfere with console operations
15. **Permission Fallback**: System shall provide alternative notification methods if browser notifications are blocked

## Success Criteria

### Measurable Outcomes
- Browser notifications are delivered at the correct times with 95%+ accuracy
- Background scheduler runs without blocking console operations 100% of the time
- System correctly handles notification permission requests and denials
- All existing 9 features continue to work without regression when reminder system is enabled
- Users can successfully set and receive notifications for their tasks

### User Experience Metrics
- Users can set reminder times in under 30 seconds
- Notification delivery is timely (within 1 minute of scheduled time)
- Users can identify tasks with active reminders at a glance in task lists
- Console application remains responsive even with background scheduler running

## Key Entities
- **Task**: Extended with reminder properties (reminder_time, last_notification_sent, notifications_enabled)
- **Reminder**: Time-based trigger for notifications, calculated as due_date - reminder_time
- **NotificationScheduler**: Background service that checks for upcoming reminders and triggers notifications
- **NotificationService**: Component responsible for delivering browser notifications and handling permissions

## Technical Considerations
- Background scheduler must be thread-safe and not block console operations
- Browser notification APIs vary between browsers - system must handle differences
- System must handle cases where notifications are blocked by user settings
- Time calculations must handle various time formats and time zones appropriately
- Memory usage should remain efficient even with many scheduled reminders

## Assumptions
- Users have browsers that support web notifications
- System has access to local time for scheduling
- Users understand the concept of time-based reminders
- Console application can run background processes without blocking user interaction
- Network connectivity is available for browser-based notifications (if needed)