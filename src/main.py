class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False


def add_task(tasks):
    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    task = Task(title)
    tasks.append(task)
    print("Task added successfully.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{index}. {task.title} - {status}")


def complete_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1].completed = True
            print(f"Task '{tasks[number - 1].title}' marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"Task '{deleted_task.title}' deleted.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()