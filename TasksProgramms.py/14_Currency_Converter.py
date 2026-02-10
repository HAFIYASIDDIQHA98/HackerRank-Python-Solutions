def currency_converter():
    # Exchange rates based on 1 USD
    exchange_rates = {
        "INR": 83.15,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 148.50
    }
    
    amount = float(input("Enter amount in USD: "))
    print("Available Currencies: INR, EUR, GBP, JPY")
    target = input("Target Currency: ").upper()
    
    if target in exchange_rates:
        converted = amount * exchange_rates[target]
        print(f"💰 {amount} USD = {converted:.2f} {target}")
    else:
        print("Currency not supported.")

currency_converter()
