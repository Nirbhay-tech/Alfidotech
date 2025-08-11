import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the TODO_FILE."""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            for line in f:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    """Saves tasks to the TODO_FILE."""
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task_description):
    """Adds a new task to the list."""
    tasks = load_tasks()
    tasks.append(task_description)
    save_tasks(tasks)
    print(f"Task '{task_description}' added.")

def view_tasks():
    """Displays all tasks in the list."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the list.")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print("-----------------------\n")

def remove_task(task_index):
    """Removes a task from the list by its index."""
    tasks = load_tasks()
    try:
        index = int(task_index) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to handle command-line arguments."""
    while True:
        print("\nCommands: add, view, remove, exit")
        command = input("Enter command: ").lower().strip()

        if command == "add":
            task_description = input("Enter task description: ")
            if task_description:
                add_task(task_description)
            else:
                print("Task description cannot be empty.")
        elif command == "view":
            view_tasks()
        elif command == "remove":
            task_index = input("Enter the number of the task to remove: ")
            remove_task(task_index)
        elif command == "exit":
            print("Exiting To-Do List app.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()