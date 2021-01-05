# Write a program to read two strings and perform concatenation and comparison operations on it.

s1 = input("string 1:\n")
s2 = input("String 2:\n")

concatenate = input("enter c for concatenate else enter n:\n") == "c"

if concatenate:
    print(s1+s2)
else:
    print("They are", ("same" if s1==s2 else "different"))
