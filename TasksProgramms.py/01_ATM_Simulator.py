# Simple ATM Logic: Deposit, Withdraw, and Balance Check
balance = 1000

print("--- Welcome to Python Bank ---")
print("1. Check Balance\n2. Deposit\n3. Withdraw")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    print(f"Current Balance: {balance}")
elif choice == '2':
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print(f"Update Balance: {balance}")
elif choice == '3':
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Remaining Balance: {balance}")
    else:
        print("Insufficient funds!")
else:
    print("Invalid choice")
