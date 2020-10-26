# Question:

# WAP to find area of a triangle using Heron's Formula

# Code:

# First we specify variables for sides of triangle
# I have used 'float' here because side values can be decimal
side1=float(input('Enter length of first side: '))
side2=float(input('Enter length of second side: '))
side3=float(input('Enter length of third side: '))

# We know s=(a+b+c)/2, so...
s=(side1+side2+side3)/2

# Now, we need to create a variable for area and enter the Heron's Formula
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5

# A statement to tell the user the area of the triangle
print(f'{area} is the area of the triangle.')

# Addtional Comments:
    # I have used formatted strings but you can use the normal method which is mentioned in next line...
    # print(area,'is the area of traingle')

# OUTPUT :-
# Enter length of first side: 4
# Enter length of second side: 5
# Enter length of third side: 6
# 9.921567416492215 is the area of the triangle.