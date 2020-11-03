# Question
# 25.	Write a program to reverse a list of integers

# Code
x = []
while True:
    print("int",str(len(x)+1)+ ':')
    i = input()
    if i != 'n' and i.strip().replace(' ','') != '' and i.isdigit():
        x.append(int(i))
    else: break

y = []
for e in x: y.insert(0, e)
print("New list:",y)
# Input
#   int 1:
#   2
#   int 2:
#   3
#   int 3:
#   4
#   int 4:
#   None
#   New list: [4, 3, 2]

# Additional Comments
#   if no digit is entered or letter is entered then end list