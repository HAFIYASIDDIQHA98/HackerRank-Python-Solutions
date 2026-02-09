def task_manager():
    print("--- ✅ Simple Task Manager ---")
    
    while True:
        choice = input("\n1. Add Task\n2. View Tasks\n3. Exit\nChoose: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            with open("tasks.txt", "a") as file:
                file.write(task + "\n")
            print("Task saved successfully!")
            
        elif choice == '2':
            print("\nYour Pending Tasks:")
            try:
                with open("tasks.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No tasks found. Create one first!")
                
        elif choice == '3':
            break
        else:
            print("Invalid Option!")

task_manager()
