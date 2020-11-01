# Question:
#13.	Write a program to check if the given string is a palindrome or not.
#
# Code:
#
#

a = input("String to check:\n").lower(); print(a,"is a palindrome") if a == a[::-1] else print(a, "is not a palindrome")
