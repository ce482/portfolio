import os

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
    return [task.strip() for task in tasks]

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display the menu
def show_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Function to mark a task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num] = tasks[task_num] + " (Completed)"
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Main function to run the app
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
