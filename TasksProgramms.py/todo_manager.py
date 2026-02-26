def show_menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. Task Add Karein")
    print("2. Tasks Dekhein")
    print("3. Exit")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Option chunein (1/2/3): ")
        
        if choice == '1':
            new_task = input("Task ka naam likhein: ")
            tasks.append(new_task)
            print("Task add ho gaya!")
        elif choice == '2':
            print("\nAapki List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == '3':
            print("Alvida!")
            break
        else:
            print("Invalid option, phir se try karein.")

if __name__ == "__main__":
    main()
