# Question
# 16.	Write a program to check whether a number is an Armstrong number

# Code

a = input("Number:\n")
sum = 0
pwr = (3 if input("Enter y for power 3 or n for power digit length") == "y" else len(a))
for digit in a: sum += int(digit) ** pwr

print("Armstrong Number") if sum == int(a) else print("Not an armstrong number")

# Output
#   Number:
#   153
#   Armstrong Number