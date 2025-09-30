def income_tax(income):
    percent = 0
    calculated_tax = 0
    if income > 132_406:
        percent = 28
        calculated_tax = round(income * percent / 100)
        print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
    elif income > 42_707:
        percent = 25
        calculated_tax = round(income * percent / 100)
        print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
    elif income > 15_527:
        percent = 15
        calculated_tax = round(income * percent / 100)
        print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
    else:
        print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")


person_income = int(input())
income_tax(person_income)
