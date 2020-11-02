# Question
# 23.	Write a program that should prompt the user to type some sentences. It should then print number of words, number of characters, number of digits and number of special

# Code
import string
s = input("String:\n")
d = 0
l = 0
sc = 0
for x in s:
    if x in string.ascii_letters: l += 1
    elif x in string.digits: d += 1
    elif x in string.punctuation: sc += 1
    else: print("Unknown character:", sc)

print("digits:",d,"letters:",l,"special characters:",sc)
# Input
#   String:
#   wlfjhwjegf*&%^$%#$^0970987320
#   digits: 10 letters: 10 special characters: 9


# Additional Comments
#   this syntax of if is correct
