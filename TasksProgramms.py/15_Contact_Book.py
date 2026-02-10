contacts = {"Hafiya": "9030108465", "Office": "1234567890"}

def contact_book():
    while True:
        action = input("\n1. Add 2. Search 3. Delete 4. Exit: ")
        if action == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            contacts[name] = phone
        elif action == '2':
            name = input("Search Name: ")
            print(f"Number: {contacts.get(name, 'Not Found')}")
        elif action == '3':
            name = input("Delete Name: ")
            if name in contacts:
                del contacts[name]
                print("Deleted!")
        elif action == '4':
            break

contact_book()
