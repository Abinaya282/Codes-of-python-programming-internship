class ToDoList:
    def __init__(self):
        self.tasks={}
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_id, task in self.tasks.items():
                print(f"{task_id}.{task['name']}-{task['status']}")
    def add_task(self):
        task_name=input("Enter task name:")
        task_id=len(self.tasks)+1
        self.tasks[task_id]={"name":task_name,"status":"Pending"}
        print("Task added successfully.")
    def update_task(self):
        self.display_tasks()
        task_id=int(input("Enter task ID to update:"))
        if task_id in self.tasks:
            task_status=input("Enter new status(Pending/Done):")
            self.tasks[task_id]["status"]=task_status
            print("Task updated successfully.")
        else:
            print("Invalid task ID.")
    def delete_task(Self):
        self.display_tasks()
        task_id=int(input("Enter task ID to delete:"))
        if task_id in self.tasks:
            del self.tasks[task_id] 
            print("Task deleted successfully.")
        else:
            print("Invalid task ID.")
def main():
    todo_list=ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice=input("Enter your choice:")
        if choice=="1":
            todo_list.display_tasks()
        elif choice=="2":
            todo_list.add_task()
        elif choice=="3":
            todo_list.update_task()
        elif choice=="4":
            todo_list.delete_task()
        elif choice=="5":
            break
        else:
            print("Invalid choice.Please try again.")
if __name__=="__main__":
    main()