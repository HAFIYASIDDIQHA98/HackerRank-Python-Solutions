def payroll_system():
    # List of Dictionaries (Real-world data format)
    employees = [
        {"id": 101, "name": "Hafiya", "salary": 85000},
        {"id": 102, "name": "Arif", "salary": 45000},
        {"id": 103, "name": "Sana", "salary": 60000}
    ]

    print("--- 💸 Employee Payroll Report ---")
    tax_rate = 0.10  # 10% Tax

    for emp in employees:
        tax_amount = emp["salary"] * tax_rate
        net_salary = emp["salary"] - tax_amount
        
        print(f"ID: {emp['id']} | Name: {emp['name']}")
        print(f"Gross: ${emp['salary']} | Tax: ${tax_amount} | Net: ${net_salary}")
        print("-" * 30)

payroll_system()
