'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = float(input("investment amount: "))
interest_rate = float(input("interest rate in percentage: ")) / 100
years = int(input("Number of years: "))
future_values = ((amount * interest_rate) * years) + amount
print("In", years, "your", amount, "will be worth", future_values)

