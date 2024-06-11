class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        description = input("Enter the task description: ")
        new_task = Task(len(self.tasks) + 1, description)
        self.tasks.append(new_task)
        print("Task created succesfully!")

    def read_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(f"ID: {task.id}, Description: {task.description}")

    def update_task(self):
        task_id = int(input("Enter the ID of the task you want to update: "))
        for task in self.tasks:
            if task.id == task_id:
                new_description = input("Enter the new task description: ")
                task.description = new_description
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self):
        task_id = int(input("Enter the ID of the task you want to delete: "))
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found!")

task_manager = TaskManager()
while True:
    print("\nMenu:")
    print("1. Create Task")
    print("2. Read Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Select an option: "))

    if choice == 1:
        task_manager.create_task()
    elif choice == 2:
        task_manager.read_tasks()
    elif choice == 3:
        task_manager.update_task()
    elif choice == 4:
        task_manager.delete_task()
    elif choice == 5:
        break
    else:
        print("Invalid choice, Please try again.")
