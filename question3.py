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
            for idx, task in enumerate(tasks, 1):
                status = "[X]" if task["completed"] else "[ ]"
                print(f"{idx}. {status} {task['name']} - Priority: {task['priority']}")
                
    elif choice == '3':
        try:
            num = int(input("Enter task number to mark complete: "))
            tasks[num-1]["completed"] = True
            print(f"Task {num} marked as complete.")
        except (ValueError, IndexError):
            print("Invalid task number.")
            
    elif choice == '4':
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num-1)
            print(f"Deleted: {removed['name']}")
        except (ValueError, IndexError):
            print("Invalid task number.")
    else:
        print("Invalid choice, please try again.")

# Final Summary
completed_count = sum(1 for t in tasks if t["completed"])
pending_count = len(tasks) - completed_count

print("\n" + "="*20)
print("FINAL SUMMARY")
print(f"Completed: {completed_count}")
print(f"Pending:   {pending_count}")
print("="*20)
print("Goodbye!")
