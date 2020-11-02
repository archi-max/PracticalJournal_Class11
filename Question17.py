# Question
# 17.	Write a menu driven program to find the area of circle, square, rectangle & triangle.

# Code

types = ["circle", "square", "rectangle", "triangle"]

print("-"*15) # 15 is length of Area Calculator. not intentional though it was a random rumber
print("Area Calculator")
print("-"*15)
print()
print("Please enter the following numbers according to the shape you want to calculate the area of.")
print()
for i, type in enumerate(types): print(i, ":", types[i])
print()
shape = int(input())

if types[shape] == "circle":
    r = float(input("Randius:\n"))
    print("Area:", 22 / 7 * r * r)

elif types[shape] == "square":
    a = float(input("Side length pls:\n"))
    print("Area:", a**2)

elif types[shape] == "rectangle":
    s1 = float(input("Side 1:\n"))
    s2 = float(input("Side 2:\n"))
    print("Area:",s1*s2)

elif types[shape] == "triangle":
    s1 = float(input("Side 1:\n"))
    s2 = float(input("Side 2:\n"))
    s3 = float(input("Side 3:\n"))

    s = (s1 + s2 + s3) / 2
    print(s)
    print(s * (s-s1) * (s-s2) * (s-s3) )
    print("Area:", ( s * (s-s1) * (s-s2) * (s-s3) ) ** 0.5 )

# Output
#
#   ---------------
#   Area Calculator
#   ---------------
#
#   Please enter the following numbers according to the shape you want to calculate the area of.
#
#   0 : circle
#   1 : square
#   2 : rectangle
#   3 : triangle
#
#   3
#   Side 1:
#   5
#   Side 2:
#   5
#   Side 3:
#   3
#   6.5
#   51.1875
#   Area: 7.1545440106270926

# Additional Comments:
#   None