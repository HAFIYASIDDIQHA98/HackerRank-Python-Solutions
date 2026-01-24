# FactSet Mock Test #3: Data Cleaning & Validation
raw_transactions = [100.5, 200.0, -50.0, 100.5, 350.75, -10.0, 500.0, 200.0]

# 1. SET Logic: Remove Duplicates
unique_transactions = set(raw_transactions)

# 2. LIST COMPREHENSION: Remove Negative values (Cleaning)
# We only want positive transactions
cleaned_transactions = [t for t in unique_transactions if t > 0]

# 3. DICTIONARY Logic: Categorize Transactions
# Let's label them: 'High' if > 300, else 'Normal.'
transaction_report = {t: ("High" if t > 300 else "Normal") for t in cleaned_transactions}

print(f"Original Data: {raw_transactions}")
print(f"Cleaned (Unique & Positive): {cleaned_transactions}")
print(f"Transaction Report: {transaction_report}")

# Bonus: Calculate total balance after cleaning
total_balance = sum(cleaned_transactions)
print(f"Final Cleaned Balance: ${total_balance}")
