# Question
# 36.	Write a program to sort a list of integers using bubble sort.

# Code
a = input("List of integers sep with commas:\n")
ints = [int(i.strip()) for i in a.split(",")]

# Bubble sorting
while True:
    swaps = False
    for x in range(len(ints)-1):
        if ints[x] > ints[x+1]:
            a, b = ints[x], ints[x+1]
            del ints[x], ints[x] # double x since after removing element at position x all elements will shift one space before
            ints.insert(x, b)
            ints.insert(x+1, a)
            swaps = True
    if not swaps: break

print("Sorted:", ints)
# Input


# Additional Comments
