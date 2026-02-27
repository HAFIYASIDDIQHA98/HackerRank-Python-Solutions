def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Test the function
print(check_even_odd(7))  # Output: 7 is Odd
