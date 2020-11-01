# Question:
#13.	Write a program to check if the given string is a palindrome or not.
#
# Code:
#
#

a = input("String to check:\n").lower(); print(a,"is a palindrome") if a == a[::-1] else print(a, "is not a palindrome")

#Input:
#   String to check:
#   me
#   me is not a palindrome

# Additional Comments:
#   ; in python is used to seperate different statements. if else can be used in this way for simple programs which do not have more than statement