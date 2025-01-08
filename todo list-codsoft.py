class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append({"task":task,"completed":False})
        print(f"Task '{task}' added successfully.")
    def view_tasks(self):
        if not self.tasks:
            print("no task found.")
        else:
            print("\n To-Do List:")
            for idx, task in enumerate(self.tasks,start=1):
                status= "Done" if task["completed"] else "pending"
                print(f'{idx}. {task["task"]} [{status}]')
    def remove_task(self,task_number):
        if 0 <task_number <= len(self.tasks):
            removed_task = removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" removed!')
        else:
            print("Invalid task number!")
    def mark_completed(self,task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'task "{self.tasks[task_number - 1]["task"]}" marked as completed!')
        else:
            print("Invalid task number!")
def main():
    todo_list = ToDoList()
    while True:
        print("\n choose an option:")
        print("1.Add Task")
        print("2.view Tasks")
        print("3.remove Task")
        print("4.Mark Task as Completed")
        print("5.Exit")

        choice = input("Enter The choice(1-5):")
        if choice == "1":
            tasks = input("Enter the task:")
            todo_list.add_task(tasks)
        elif choice  == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to remove:"))
                todo_list.remove_task(task_number)
            except ValueError:
                print("please enter a valid number!")
        elif choice == "4":
            try:
                task_number = int(input("Enter the task number to mark as completed:"))
                todo_list.mark_completed(task_number)
            except ValueError:
                print("please enter a valid number!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! please select a valid option.")
if __name__ == "__main__":
    main()


      

        
    



                