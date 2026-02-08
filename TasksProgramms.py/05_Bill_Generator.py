# Simple Bill Generator with GST (Tax) calculation
items = []
prices = []

print("--- Welcome to SuperMart ---")
while True:
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Enter price for {item}: "))
    items.append(item)
    prices.append(price)

# Calculations
subtotal = sum(prices)
tax = subtotal * 0.18  # 18% GST
total = subtotal + tax

print("\n--- YOUR FINAL BILL ---")
for i in range(len(items)):
    print(f"{items[i]}: ₹{prices[i]}")

print("-" * 20)
print(f"Subtotal: ₹{subtotal}")
print(f"GST (18%): ₹{tax:.2f}")
print(f"Grand Total: ₹{total:.2f}")
