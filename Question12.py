# Question

# WAP to find a reverse of the four-digit number

# Code

# I ask the user for the number
num=int(input('Enter a number: '))

# I initialize the value to null ; rev is just another variable I took for reverse
rev=0

# we can do the task by using a while loop
while (num>0):   # 'num' should not be reversed otherwise there is no reverse

    # Here we divide the value of num which helps to store first digit in one's place, second digit in ten's place and so on
    digit=num%10
    rev=rev*10+digit

    # Now the last digit is removed by divind the number with 10 with no decimal
    num=num//10

# Now we simply print the reverse of digit
print(f'Reverse number is {rev}')



