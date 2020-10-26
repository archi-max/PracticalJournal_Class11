# Question:


#WAP to find the largest of the 3 numbers


# CODE:-

# I have used FLOAT here so it can tell the largest even if it's a decimal

num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
num3=float(input('Enter third number: '))

# Here I used a simple if,elif and else statement
# I have taken Largest as a variable for the largest number
if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num3) and (num2>=num1):
    largest=num2
else:
    largest=num3
print(f'Largest number is: {largest}')

# OUTPUT :
# Enter first number: 25
# Enter second number: 50
# Enter third number: 24
# Largest number is: 50.0


# Addtional comments::
# In line 23, I have used formatted strings, but you can write it in simpler way as well. Check next line
# print("Largest number is: ",largest)