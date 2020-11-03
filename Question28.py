# Question
# 28.	Write a program to print the following shape:

# Code
# s = ''
for x in range(1,5):
    s = '*' * x
    # s[-y:] = ''
    print(s)
print('\n')

for x in range(1,6):
    n = x if x <= 3 else 6-x
    s = '*' * n
    # s[-y:] = ''
    print(s)
print()
for x in range(5,0,-1):
    s = ''.join([str(l) for l in range(5,0,-1)])
    print(s[:x])
# Input
# *
# **
# ***
# ****
#
#
# *
# **
# ***
# **
# *
#
# 54321
# 5432
# 543
# 54
# 5

# Additional Comments