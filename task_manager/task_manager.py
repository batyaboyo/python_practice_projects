import os

def display_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Help")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\nEnter task: ")
    tasks.append(task)
    print("Task added successfully.")

def mark_completed(tasks):
    view_tasks(tasks)
    index = int(input("\nEnter the index of the task to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index] += " - Completed"
        print("Task marked as completed.")
    else:
        print("Invalid index.")

def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("\nEnter the index of the task to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully.")
    else:
        print("Invalid index.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice =='5':
            print('\nThis a command line based task manager app to help you be more productive and finish tasks in time.')
            print('''           
           To use this task Manager choose.....
           
           1 to view tasks
           
           2 to add tasks 
           
           3 to mark tasks complete
           
           4 to delete a task
           
           5 to get help
           
           6 to exit app
            ''')
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()