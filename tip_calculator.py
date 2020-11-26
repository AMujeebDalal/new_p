#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
t = input("What was the total bill? $")
p = input("What percentage tip would you like to give? 10, 12, or 15? ")
s = input("How many people to split the bill? ")
t1 = int(t)
p1 = int(p)
t2 = t1 + t1 * p1/100
pay = round(t2 / int(s),2)
print(f"Each person should pay: ${pay}")
