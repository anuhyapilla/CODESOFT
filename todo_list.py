def show_menu():
    print("\n------ To-Do List ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

tasks = []

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(f"✅ Task '{task}' added!")
    else:
        print("❌ Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\nAll Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔ Done" if t["done"] else "❌ Pending"
        print(f"{i}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index-1]["done"] = True
            print(f"✅ Task '{tasks[index-1]['task']}' marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index-1)
            print(f"✅ Task '{removed['task']}' deleted!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main program
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("❌ Invalid option. Try again.")
