# Question:-

# WAP to perform all the mathematical operations on a set of values :-

# Code:-

# We will ask the user to give 2 values and we will perform +, -, x, / operations on those 2
num1=int(input('Enter a number: '))
num2=int(input('Enter a number: '))

# Now we just add formulas for the operations
sum_num=num1+num2
diff_num=num1-num2
pro_num=num1*num2
divide_num=num1/num2

# Now we print these values
print(f'Sum of {num1} and {num2} is {sum_num}')
print(f'Difference of {num1} and {num2} is {diff_num}')
print(f'Product of {num1} and {num2} is {pro_num}')
print(f'Quotient of {num1} and {num2} is {divide_num}')

# Addtional comments:-
    # I used formatted strings but you can use print statement in whatever way you find comfortable. Check next line...
    # For example - print('Sum of ',num1 ,'and ',num2 ,'is ',sum_num.)

# OUTPUT :-
# Enter a number: 4
# Enter a number: 2
# Sum of 4 and 2 is 6
# Difference of 4 and 2 is 2
# Product of 4 and 2 is 8
# Quotient of 4 and 2 is 2.0
