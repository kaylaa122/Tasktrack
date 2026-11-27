# TaskTrack

TaskTrack is a command-line task manager created for CPS 310.
# TaskTrack

TaskTrack is a simple command-line program that lets users manage tasks.

## Current Features
- Add tasks
- View tasks
- Save tasks to tasks.txt
- Load saved tasks when the program starts
- Prevent empty tasks from being added

## Running the Program
Open a terminal in the TaskTrack project folder and run:
- python tasktrack.py
- Task Persistence
Tasks are loaded from tasks.txt when the program starts. When a user adds a new task, the updated task list is saved to the file. This allows tasks to remain available after the program closes.

## How It Works

TaskTrack uses a Python list to manage tasks while the program is running. The program loads previously saved tasks when it starts and saves new tasks to tasks.txt.

## Current Limitations

- Users cannot delete tasks yet.
-Users cannot edit existing tasks yet.

## Version Control

TaskTrack uses Git to track project changes. Git records commits locally, while push uploads changes to GitHub and pull downloads and integrates changes from GitHub.