# Question
# 18.	Write a program that reads a number of seconds and prints it in form: min and seconds. Eg 200 mins are printed as 3 mins 20 seconds.

# Code

a = float(input("Time in Seconds:\n "))
print("Time in minutes: {} minutes {} seconds".format(a//60, a%60) ) # // divides

# Input
#   Time in Seconds:
#    230.1
#   Time in minutes: 3.0 minutes 50.099999999999994 seconds

# Additional Comments:
#   None