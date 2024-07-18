# todo_list.py

import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i+1}. {task['task']} - {status}")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            print("Invalid task index.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index.")

    def mark_task_incomplete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = False
        else:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            print("File not found. Starting with an empty to-do list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Mark Task Incomplete")
        print("7. Save Tasks")
        print("8. Load Tasks")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == '6':
            task_index = int(input("Enter the task number to mark as incomplete: ")) - 1
            todo_list.mark_task_incomplete(task_index)
        elif choice == '7':
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '8':
            filename = input("Enter the filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
