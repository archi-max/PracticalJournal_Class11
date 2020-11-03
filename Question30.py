# Question
# 30.	Write a program to read a list of ‘n’ integers from the user. Create two new lists, one having all positive numbers and the other having all negative numbers.  Print all three lists

# Code
x = []
n = 5
for e in range(n):
    a = input(f"int {e}:\n")
    while not a.replace('+','').replace('-','').isdigit():
        a = input(f"int {e}:\n")
    a = int(a)
    x.insert(e, a)

lp = []
ln = []

for e in x: lp.append(e) if e > 0 else ln.append(e)

print("Original list")
[print('+'+str(e)) for e in x if e > 0]
[print(str(e)) for e in x if e < 0]
print("Positive integers")
[print('+'+str(e)) for e in lp]
print("Negative integers")
[print(e) for e in ln]

# Input
#   int
#   0:
#   1
#   int
#   1:
#
#   int
#   1:
#   wef
#   int
#   1:
#   wrfe
#   int
#   1:
#   wef
#   int
#   1:
#   3
#   int
#   2:
#   1
#   int
#   3:
#   -1
#   int
#   4:
#   3
#   Original
#   list
#   +1
#   +3
#   +1
#   +3
#   -1
#   Positive
#   integers
#   +1
#   +3
#   +1
#   +3
#   Negative
#   integers
#   -1

# Additional Comments
