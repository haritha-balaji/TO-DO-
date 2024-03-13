class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += " (Complete)"
            print(f"Task '{self.tasks[task_index]}' marked as complete.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
        if not self.tasks:
            print("No tasks.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Mark Task Complete\n3. View Tasks\n4. Remove Task\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
