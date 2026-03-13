tasks = []

print("--- To-Do List Manager ---")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Select an option (1-5) or type 'exit': ").strip().lower()
    
    if choice in ['5', 'exit']:
        break
        
    elif choice == '1':
        name = input("Enter task name: ").strip()
        priority = input("Enter priority (e.g., High, Medium, Low): ").strip().capitalize()
        tasks.append({"name": name, "priority": priority, "completed": False})
        print(f"Task '{name}' added.")
        
    elif choice == '2':
        if not tasks:
            print("Your list is empty.")
        else:
            print("\nCurrent Tasks:")
            count = 1
            for task in tasks:
                status = "[X]" if task["completed"] else "[ ]"
                print(f"{count}. {status} {task['name']} - Priority: {task['priority']}")
                count += 1
                
    elif choice == '3':
        if not tasks:
            print("Your list is empty. Nothing to mark as complete.")
        else:
            num_input = input("Enter task number to mark complete: ").strip()
            if num_input.isdigit():
                num = int(num_input)
                if 0 < num <= len(tasks):
                    tasks[num-1]["completed"] = True
                    print(f"Task {num} marked as complete.")
                else:
                    print("Task number out of range.")
            else:
                print("Invalid input. Please enter a number.")
            
    elif choice == '4':
        if not tasks:
            print("Your list is empty. Nothing to delete.")
        else:
            num_input = input("Enter task number to delete: ").strip()
            if num_input.isdigit():
                num = int(num_input)
                if 0 < num <= len(tasks):
                    removed = tasks.pop(num-1)
                    print(f"Deleted: {removed['name']}")
                else:
                    print("Task number out of range.")
            else:
                print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice, please try again.")

completed_count = 0
pending_count = 0

for task in tasks:
    if task["completed"]:
        completed_count += 1
    else:
        pending_count += 1

print("\n" + "="*20)
print("FINAL SUMMARY")
print(f"Completed Tasks: {completed_count}")
print(f"Pending Tasks:   {pending_count}")
print("="*20)
print("Goodbye!")
