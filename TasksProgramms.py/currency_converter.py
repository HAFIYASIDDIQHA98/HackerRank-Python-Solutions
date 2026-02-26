def currency_converter():
    # Fixed Exchange Rates (Base: 1 USD)
    rates = {
        "INR": 83.50,  # 1 USD = 83.50 INR
        "EUR": 0.92,   # 1 USD = 0.92 EUR
        "GBP": 0.78    # 1 USD = 0.78 GBP
    }

    print("--- CURRENCY CONVERTER (USD to Others) ---")
    try:
        usd_amount = float(input("USD mein amount likhein: $"))
        
        print("\nConvert karne ke liye option chunein:")
        for currency in rates.keys():
            print(f"- {currency}")

        choice = input("\nTarget currency ka naam likhein (e.g., INR): ").upper()

        if choice in rates:
            converted = usd_amount * rates[choice]
            print(f"\nResult: ${usd_amount} USD = {converted:.2f} {choice}")
        else:
            print("Maaf kijiye, ye currency abhi available nahi hai.")
            
    except ValueError:
        print("Error: Kirpya sirf numbers ka istemal karein!")

currency_converter()
