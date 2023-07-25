#this method calculate the amount of money you need to pay, including the tip
print("welcome to the tip calculator.")
bill = input("what was the total bill? $")
bills = float(bill)
percentage = input("what percentage tip you would like to give? 10, 12 or 15? ")
percentages = int(percentage)
how_many = input("how many pepole to split the bill? ")
how_manys = int(how_many)
each = bills / how_manys
each += ((bills / 100) * percentages) / how_manys
each = round(each, 2)
print(f"each person should pay: {each}")

