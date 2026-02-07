# Storing and searching student records
students = {
    "Hafiya": {"Roll": 101, "Grade": "A"},
    "Ali": {"Roll": 102, "Grade": "B"},
    "Sara": {"Roll": 103, "Grade": "A+"}
}

name = input("Enter student name to search: ")

# .get() use karna professional hai taaki error na aaye
record = students.get(name)

if record:
    print(f"Record Found: {name}'s Roll No is {record['Roll']} and Grade is {record['Grade']}")
else:
    print("Record not found in our database.")
