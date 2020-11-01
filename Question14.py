# Question
# 14.	Write a program to input 3 sides of a triangle and prints whether it is an equilateral, isosceles or scale triangle.
#
# Code
#

sides = [int(input("Side "+str(n)+" :\n")) for n in  range(3)]
s1, s2, s3 = sides #Too lazy to repeat the same thing. lol.

is_triangle = [s1+s2 > s3, s2 + s3 > s1, s3 + s1 > s2] #List of conditions to check

if all(is_triangle):
    if s1 == s2 == s3:
        print("Equivalent triangle")
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print("isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle!")


# Output:
#   Side 0 :
#   6
#   Side 1 :
#   6
#   Side 2 :
#   6
#   Equivalent triangle

#Additional Comments:
# all checks if all conditions r true from a list.
