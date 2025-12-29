# Quickstart: Todo In-Memory Python Console Application

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, for dependency management)
- Terminal/command prompt access

## Setup Instructions

### 1. Clone or Download the Project
```bash
# If cloning from repository
git clone <repository-url>
cd <project-directory>
```

Or download and extract the project files to your local directory.

### 2. Verify Python Version
```bash
python --version
# Should show Python 3.13.x or higher
```

### 3. Navigate to Project Directory
```bash
cd src/
```

## Running the Application

### Method 1: Direct Python Execution
```bash
python main.py
```

### Method 2: Using Python Module (if __main__.py exists)
```bash
python -m main
```

## Basic Usage

Once the application starts, you'll see the main menu:

```
==================================================
TODO APPLICATION - MAIN MENU
==================================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit
==================================================
```

### Test the Application
1. Select option 1 to add a test task
2. Select option 2 to view tasks
3. Select option 6 to exit

## Testing Functionality

### Run the Built-in Test Script
```bash
python ../test_functionality.py
```

This will execute all 5 core features and verify they work correctly.

### Manual Testing Steps
1. **Add Task**: Enter title and description
2. **View Tasks**: Verify task appears in list
3. **Update Task**: Modify existing task
4. **Delete Task**: Remove a task
5. **Mark Complete/Incomplete**: Toggle task status

## Troubleshooting

### Common Issues
- **Python version too old**: Upgrade to Python 3.13+
- **Module not found**: Ensure you're running from the src directory
- **Permission errors**: Check file permissions on main.py

### Verify Installation
```bash
# Test Python import
python -c "from main import TodoApp; print('Import successful')"
```