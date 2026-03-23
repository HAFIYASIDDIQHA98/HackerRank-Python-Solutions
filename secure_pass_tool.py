import random
import string
import re

def check_strength(password):
    if len(password) < 8: return "Weak (Too short)"
    if not re.search("[a-z]", password): return "Weak (No lowercase)"
    if not re.search("[A-Z]", password): return "Medium (Add uppercase)"
    if not re.search("[0-9]", password): return "Medium (Add numbers)"
    if not re.search("[!@#$%^&*]", password): return "Strong (Add symbols for extra safety)"
    return "Very Strong"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(length))

# Main logic
print("--- Password Tool ---")
choice = input("1. Generate Password\n2. Check Strength\nSelect (1/2): ")

if choice == '1':
    len_input = int(input("Enter length: "))
    print(f"Generated Password: {generate_password(len_input)}")
elif choice == '2':
    pwd = input("Enter password to check: ")
    print(f"Strength: {check_strength(pwd)}")
