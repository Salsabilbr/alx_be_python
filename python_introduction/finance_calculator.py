monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("4000: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}")
