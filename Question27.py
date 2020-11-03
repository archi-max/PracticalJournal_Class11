# Question
# 27. Ask the user to enter a list of strings. Create a new list that contains only those strings which start with a vowel.

# Code
s = input("String:\n")
for vowel in "aeiou": s = s.replace(vowel, "*")
print("New string:",s)
# Input
#   string:
#   wefjnopgqurb
#   New string: w*fjn*pgq*rb

# Additional Comments