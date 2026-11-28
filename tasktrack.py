"""A command-line task manager created for CPS 310.

Author: Kemi Olusi

Course: CPS 310
"""
def load_tasks():
    """Load tasks from the tasks.txt file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the tasks.txt file."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
 

def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return
     
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

def remove_task(tasks):
    """Prompt the user to select and remove a task."""

    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)

    selection = input("Enter the number of the task to remove: ").strip()

    if not selection.isdigit():
        print("Please enter a valid task number.")
        return False

    task_number = int(selection)

    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return False

    removed_task = tasks.pop(task_number - 1)

    print(f"Removed task: {removed_task}")

    return True

def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            if remove_task(tasks):
                save_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()



def remove_task(tasks):
    """Prompt the user to select and remove a task."""

    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)

    selection = input("Enter the number of the task to remove: ").strip()

    if not selection.isdigit():
        print("Please enter a valid task number.")
        return False

    task_number = int(selection)

    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return False

    removed_task = tasks.pop(task_number - 1)

    print(f"Removed task: {removed_task}")

    return True

def load_tasks():
    """Load tasks from the tasks.txt file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the tasks.txt file."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

 

def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return
     
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

