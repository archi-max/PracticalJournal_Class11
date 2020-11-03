# Question
# 37.	Write a program to perform sorting on the given list of strings, on the basis of length of strings

# Code

a = input("List of strings, sep with commas:\n")
strings = [i.strip() for i in a.split(",")]

strings.sort(key=lambda x: len(x))

print("Sorted strings")
print(strings)
# Input
#   List of strings, sep with commas:
#   awfwefwef, a, aass, awdf, adwefwefgwgw, asedf
#   Sorted strings
#   ['a', 'aass', 'awdf', 'asedf', 'awfwefwef', 'adwefwefgwgw']

# Additional Comments
# lambda is used to define functions inline.
