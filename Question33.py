# Question
# 33.	Write a program to accept age of employees & count the number of employees  in  the following age groups.
# i.	a.  26-35        b.  36-45       c.  46-55

# Code

l1 , l2, l3 = [], [], []
a = input("Please enter age sepearted by commas:\n")

for x in a.split(","):
    x = int(x)
    if x in range(26, 36): l1.append(x)
    if x in range(36, 46): l2.append(x)
    if x in range(46, 56): l3.append(x)

print("26 - 35:", len(l1))
print(*l1, sep=", ") # Finally a use for sep!
print("36 - 45:", len(l2))
print(*l2, sep=", ")
print("46 - 55:", len(l3))
print(*l3, sep=", ")
# Input
#   26, 27, 28, 36, 37, 38, 46, 47, 48
#   26 - 35
#   26, 27, 28
#   36 - 45
#   36, 37, 38
#   46 - 55
#   46, 47, 48

# Additional Comments
