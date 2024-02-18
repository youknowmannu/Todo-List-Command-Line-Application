class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def delete_task(self, task_index):
        del self.tasks[task_index]

    def complete_task(self, task_index):
        self.tasks[task_index]['completed'] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{index + 1}. {task['task']} - {status}")
                
def main():
    todo_list = TodoList()

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. View To-Do List")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            if todo_list.tasks:
                print("Current To-Do List:")
                todo_list.display_tasks()
                task_index = int(input("Enter the index of the task to delete: ")) - 1
                if 0 <= task_index < len(todo_list.tasks):
                    todo_list.delete_task(task_index)
                    print("Task deleted successfully!")
                else:
                    print("Invalid task index.")
            else:
                print("No tasks to delete.")
        elif choice == '3':
            if todo_list.tasks:
                print("Current To-Do List:")
                todo_list.display_tasks()
                task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
                if 0 <= task_index < len(todo_list.tasks):
                    todo_list.complete_task(task_index)
                    print("Task marked as completed!")
                else:
                    print("Invalid task index.")
            else:
                print("No tasks to mark as completed.")
        elif choice == '4':
            print("Current To-Do List:")
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()
