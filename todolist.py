# todolist.py

class ToDoList:
    """Class representing a To-Do List."""

    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        """View all tasks in the list."""
        print("To-Do List:")
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = " [ ] " if not task["completed"] else " [x] "
                print(f"{index}. {status}{task['task']}")

    def mark_complete(self, task_index):
        """Mark a task as complete."""
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        """Delete a task from the list."""
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")


# main.py

from todolist import ToDoList

def main():
    """Main function to interact with the To-Do List."""
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
