print("Welcome to the tip calculator!")

bill_total = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10,12,or 15? "))/100+1

people = int(input("How many would like to split the bill? "))

total_cost = (bill_total*tip/people)

print(f"Each person should pay: ${total_cost:.2f}")