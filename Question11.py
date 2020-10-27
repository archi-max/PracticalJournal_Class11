# Question

# WAP to get a fibonacci series till 'n' terms

# CODE :

# I ask the user to tell the number of terms
nterm=int(input('How many terms? '))

# Since fibonacci series always start wit 0 and 1...
n1,n2=0,1

# Introduced 'count' as a variable which will move on to the next value if the previous value satisfies conditons
count=0

# Since fibonacci series can never have a -ve value, it will tell the user to enter a positive value
if nterm<=-1:
    print(f'{nterm} is negative. Enter a positive value')

# If number of terms is specified as 1, then there will only be 1 value in the series i.e. 0
elif nterm==1:
    print('Fibonacci Series: ')
    print(n1)

# For the number of terms =>2...
else:
    print('Fibonacci Series: ')
    # Here we want the series to be only as ling as specified by the user, so count cannot exceed the number of terms
    while count<nterm:
        print(n1)
        nth=n1+n2
        # Update the values
        n1=n2
        n2=nth
        count+=1

# No addtional comments

# OUTPUT :
# How many terms? 7
# Fibonacci Series:
# 0
# 1
# 1
# 2
# 3
# 5
# 8