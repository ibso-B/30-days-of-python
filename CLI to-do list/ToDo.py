import json
import sys
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("Your to-do list is empty.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f'{number}. [{status}] {task["text"]}')


def add_task(tasks, text):
    """Add a new task."""
    if not text.strip():
        print("Please provide a task description.")
        return

    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f'Task added: "{text}"')


def mark_done(tasks, number):
    """Mark a task as completed."""
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print(f'Task {number} marked as completed.')


def delete_task(tasks, number):
    """Delete a task."""
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    removed = tasks.pop(number - 1)
    save_tasks(tasks)
    print(f'Task deleted: "{removed["text"]}"')


def main():
    tasks = load_tasks()

    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|done|delete]")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print('Usage: python todo.py add "Task description"')
            return

        text = " ".join(sys.argv[2:])
        add_task(tasks, text)

    elif command == "list":
        show_tasks(tasks)

    elif command == "done":
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print("Usage: python todo.py done <task_number>")
            return

        mark_done(tasks, int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print("Usage: python todo.py delete <task_number>")
            return

        delete_task(tasks, int(sys.argv[2]))

    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, list, done, delete")


if __name__ == "__main__":
    main()