# Question:

# WAP to find whether a year is a leap year or not:-

# Code:

# Here, we use 'int' cuz year cannot be in decimal
year=int(input('Enter year: '))

# Rest of the code is if and else statements

# These are the conditions which tell us if the year is a leap year or not
if year%4==0 and year%100!=0:
    print(f'{year} is a leap year.')
elif year%100==0:
    print(f'{year} is not a leap year.')
elif year%400==0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')

# OUTPUT :-
# Enter year: 2012
# 2012 is a leap year.


# Additional Comments:-
# I have used formatted strings, but you can do it in a way that you're comfortable.



