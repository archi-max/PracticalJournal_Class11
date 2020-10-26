# Question:

# WAP to find factorial of a number:-

# CODE:-

# For this we can import the math module which contains the method 'factorial'
# 'Factorial' of a number is all numbers multiplied till that number for ex- 3!=1x2x3=6
import math

# Here, we will use 'int' because factorial method does not accept decimal
num=int(input('Enter a number: '))

# For the output, we can simply include it in a print statement:
print(f'Factorial of {num} is ',math.factorial(num))

# Additional Comments:
    # I have used formatted strings but you use what you are comfortable with. Check next line...
    # print('Factorial of ',num,'is ',math.factorial(num))

# OUTPUT
# Enter a number: 3
# Factorial of 3 is  6