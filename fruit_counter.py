# Topic: Dictionary and Loop Logic
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for fruit in fruits:
    if fruit in word_count:
        word_count[fruit] += 1
    else:
        word_count[fruit] = 1

print("Fruit Counts:", word_count)
