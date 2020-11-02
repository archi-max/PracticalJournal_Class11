# Question
# 19.	Write a program to input a string and a character and count the number of occurrences of the input character in a given string

# Code:

a = input("String:\n")
char = input("Character:\n")
count = 0
for letter in a:
    if letter == char:
        count += 1
print("Count:",count)
# Input:
#   String:
#   abceed
#   Character:
#   e
#   Count: 2

# Additional Comments:
#   None