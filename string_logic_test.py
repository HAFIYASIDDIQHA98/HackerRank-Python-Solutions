# FactSet Mock Test #2: String Analytics
text = "learning python is fun and practicing python logic is better"

# 1. Counting Frequency
char_counts = {}
for char in text.replace(" ", ""): # Spaces remove kar diye
    char_counts[char] = char_counts.get(char, 0) + 1

# 2. List Comprehension: Characters appearing more than 3 times
frequent_chars = [char for char, count in char_counts.items() if count > 3]

# 3. Set Logic: Check if all letters of 'python' are in our text
python_set = set("python")
text_set = set(text)
has_all_python_letters = python_set.issubset(text_set)

print(f"Character Counts: {char_counts}")
print(f"Frequent Characters (>3 times): {frequent_chars}")
print(f"Does text have all 'python' letters?: {has_all_python_letters}")
