# Program to convert USD to INR and vice versa
# Current Rate: 1 USD = 83.50 INR (approx)

def convert_currency():
    rate = 83.50
    print("--- Currency Converter ---")
    print("1. USD to INR")
    print("2. INR to USD")
    
    choice = input("Select conversion (1/2): ")
    
    if choice == '1':
        usd = float(input("Enter amount in USD: "))
        print(f"${usd} = ₹{usd * rate:.2f}")
    elif choice == '2':
        inr = float(input("Enter amount in INR: "))
        print(f"₹{inr} = ${inr / rate:.2f}")
    else:
        print("Invalid choice!")

convert_currency()
