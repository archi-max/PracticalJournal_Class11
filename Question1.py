# Question:

# Write a program to compute simple interest and compound interest given principle, rate and time period.

# Code:


#Inputs
principal = float(input("Please enter the principal amount:\n"))
rate = float(input("Please enter the rate of interest:\n"))
simple_interest = input("Please enter y if simple interest else type n:\n")  # Yes or no if simple interest or compund simple_interest
duration = float(input("please enter duration of the loan in amount of years:\n"))

if simple_interest == 'y':
    total = (principal * rate * duration / 100) + principal #Total amount = principal x rate/100 x duration + principal
    print("Simple Interest:", total)

else:
    total = principal * ( (1 + (rate/100))**duration) #Total amount = principal * (1 +r/100)^duration
    print("Compound Interest:", total)

# Output:
#   input - 1000, 5.2, y, 2
#   output - 1104.0

# Additional Comments:
#      Check the compund interest formula