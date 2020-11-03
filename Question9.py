# Question :-

# WAP to find if a given number is prime or not :-

# CODE :-

# I ask the user to give a number to check if its prime or not
num=int(input('Enter a number: '))

# Primes are greater than 1
if num>1:

    # Now I introduced a range from which to check if the number is a prime or not
    for i in range(2,num):
        if num%i==0:
            print(f'{num} is not a prime number.')
            print(f'{i} times {num//i} is {num}.')
            break
    else:
        print(f'{num} is a prime number.')

# if the entered number is <= 1 or =1, then its not a prime number
else:
    print(f'{num} is not a prime number.')

# Addtional Comments
# I have used formatted strings but you can use whatever method you are comfortable with. Check next line...
# For example - print(num,'is not a prime number') or print(i,"times",num,"is",num)


# OUTPUT:-
# Enter a number: 2
# 2 is a prime number.
         # OR
# Enter a number: 4
# 4 is not a prime number.
# 2 times 4 is 4.