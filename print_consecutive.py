# Program to print numbers from 1 to n in a single line without spaces
# Example: If n=3, Output will be 123

if __name__ == '__main__':
    # Taking integer input from user
    n = int(input("Enter a number: "))
    
    # Loop from 1 to n (inclusive)
    # range(1, n+1) ensures n is also printed
    for i in range(1, n + 1):
        # end="" prevents moving to a new line after each print
        print(i, end="")

# Final print for a clean terminal exit
print()
