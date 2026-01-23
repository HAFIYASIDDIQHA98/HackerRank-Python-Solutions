# Topic: Understanding Sets and Unique Data Handling
# This is useful for removing duplicates and finding common items.

# 1. Creating a Set (Duplicates are automatically removed)
guest_list = {"Ali", "Sara", "Hafiya", "Ali", "Zane"}
print("Unique Guest List:", guest_list)

# 2. Set Operations (Skills Comparison)
python_students = {"Hafiya", "Sara", "Rahul"}
java_students = {"Hafiya", "Ali", "Kiran"}

# Find students who know BOTH (Intersection)
both_skills = python_students.intersection(java_students)
print("Students who know both Python and Java:", both_skills)

# Find ALL unique students (Union)
all_students = python_students.union(java_students)
print("Total unique students in both classes:", all_students)

# 3. Adding and Removing
python_students.add("Zane")
python_students.remove("Rahul")
print("Updated Python Students:", python_students)
