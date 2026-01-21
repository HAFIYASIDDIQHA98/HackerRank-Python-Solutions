# Program to check if a year is a Leap Year
# A year is a leap year if it is divisible by 4, 
# except for century years, which must be divisible by 400.

def is_leap(year):
    # Initializing the leap variable
    leap = False
    
    # Logic: Divisible by 4 AND (Not divisible by 100 OR divisible by 400)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        
    return leap

# Taking user input with a clear prompt
check_year = int(input("Enter a year to check for Leap Year: "))

# Result formatting
if is_leap(check_year):
    print(f"Result: {check_year} is a Leap Year.")
else:
    print(f"Result: {check_year} is not a Leap Year.")
