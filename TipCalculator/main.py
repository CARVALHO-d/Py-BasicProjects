# 1- Greetings.
print("Welcome to the tip calculator.")

# 2- Inputs: total bill; percentage tip (10, 12, 15); how many people splitting.
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100 + 1
people = int(input("How many people to split the bill? "))

# 3- Calculate how many each person should pay.
each_payment = round(bill * percentage_tip / people, 2)

# 4- Print the result.
print(f"Each person should pay: ${each_payment:.2f}")
