todo_list = []

while True:
    print("\n--- My To-Do List ---")
    print("1. Task Add karein")
    print("2. List dekhein")
    print("3. Exit")
    
    choice = input("Option select karein (1/2/3): ")
    
    if choice == '1':
        task = input("Task likhein: ")
        todo_list.append(task)
        print("Task add ho gaya!")
    elif choice == '2':
        print("\nAapke Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
