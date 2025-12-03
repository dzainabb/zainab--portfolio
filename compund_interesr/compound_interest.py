import math

def InterestCal(Savings, AnnualInterestRate, Years):
    for i in range(Years):
        Amount = Savings * math.pow((1 + AnnualInterestRate/100), i+1)
        print(f"For Year {i+1}, you will have a balance of £{Amount:.2f}")
    return Amount  # final balance

Savings = float(input("Input your savings: £"))
AnnualInterestRate = float(input("Input your interest rate (%): "))
Years = int(input("Input your number of years: "))

final_amount = InterestCal(Savings, AnnualInterestRate, Years)

print(f"\nAfter {Years} years, you will have: £{final_amount:.2f}")