import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
        return tasks if isinstance(tasks, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not read saved tasks. Starting with a fresh list.")
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2)
    except OSError:
        print("Could not save tasks to disk.")


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['title']}")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to complete.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("Select a task number to mark done: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if 0 <= choice < len(tasks):
        tasks[choice]["done"] = True
        save_tasks(tasks)
        print(f"Completed: {tasks[choice]['title']}")
    else:
        print("That task number does not exist.")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("Select a task number to remove: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if 0 <= choice < len(tasks):
        removed = tasks.pop(choice)
        save_tasks(tasks)
        print(f"Removed: {removed['title']}")
    else:
        print("That task number does not exist.")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Mark task done")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Choose a valid option from 1 to 5.")


if __name__ == "__main__":
    main()
