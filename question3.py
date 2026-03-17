"""
3)	Build a to-do list manager that
•	Allows users to add tasks with priorities (e.g., "Buy milk - high").
•	Lets them view the current list, delete tasks by number, and mark tasks as complete.
•	Keeps looping until the user types "exit".
•	Shows a summary at the end: number of completed tasks vs pending.
"""
tasks = []

print(r"""
  _____ ___        ____   ___  
 |_   _/ _ \      |  _ \ / _ \ 
   | || | | |_____| | | | | | |
   | || |_| |_____| |_| | |_| |
   |_| \___/      |____/ \___/ 
""")

while True:
    print("\n" + "═"*25)
    print("      MAIN MENU")
    print("═"*25)
    print(" 1. Add Task")
    print(" 2. View Tasks")
    print(" 3. Mark Complete")
    print(" 4. Delete Task")
    print(" 5. Exit")
    
    choice = input("\nSelect (1-5): ").strip().lower()
    
    if choice in ['5', 'exit']:
        break
        
    elif choice == '1':
        while True:
            name = input("Enter task name: ").strip()
            if name: break
            print("Name cannot be empty!")

        while True:
            p_input = input("Priority (High/Med/Low): ").strip().capitalize()
            if p_input in ["High", "Med", "Low"]:
                priority = p_input
                break
            print("    Invalid priority. Please type High, Med, or Low.")

        tasks.append({"name": name, "priority": priority, "completed": False})
        print(f"   Added: '{name}'")
        
    elif choice == '2':
        if not tasks:
            print("\n  [!] Your list is empty.")
        else:
            print(f"\n{'#':<3} {'STATUS':<8} {'TASK':<15} | {'PRIORITY'}")
            print("-" * 40)
            for i, task in enumerate(tasks, 1):
                status = "[✔]" if task["completed"] else "[ ]"

                print(f"{i:<3} {status:<8} {task['name']:<15} | {task['priority']}")
                
    elif choice == '3':
        if not tasks:
            print("\n  [!] Nothing to complete.")
            continue
            
        num_input = input("Enter number to complete: ").strip()
        
        if num_input.isdigit():
            idx = int(num_input) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["completed"] = True
                print(f"   Task '{tasks[idx]['name']}' is done!")
            else:
                print("That number isn't on the list.")
        else:
            print("Please enter a valid number.")

    elif choice == '4':
        if not tasks:
            print("\n  [!] Nothing to delete.")
            continue
            
        num_input = input("Enter number to delete: ").strip()
        
        if num_input.isdigit():
            idx = int(num_input) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                print(f"  🗑️  Removed: '{removed['name']}'")
            else:
                print("That number isn't on the list.")
        else:
            print("Please enter a valid number.")
    else:
        print(f"\n'{choice}' is not a valid option. Please pick 1-5.")
        
        
done = 0
for t in tasks:
    if t["completed"]:
        done += 1
todo = len(tasks) - done

print("\n" + "=" * 30)
print(f"   FINAL STATS")
print(f"   Completed: {done}")
print(f"   Pending:   {todo}")
print("=" * 30)
print("BYE BYE!")
