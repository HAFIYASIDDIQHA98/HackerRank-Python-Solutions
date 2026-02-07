# Program to check if a password is strong or weak
password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long = len(password) >= 8

if has_upper and has_digit and is_long:
    print("Strength: Strong Password 💪")
elif is_long:
    print("Strength: Medium (Add numbers and capital letters)")
else:
    print("Strength: Weak (Too short)")
