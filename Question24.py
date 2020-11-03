# Question
#   24.	Write a program to find the sum of the given series.
#   a.	1+2+3+…….+n
#   b.	1^2+2^2+3^2+…..+n^2
#   c.	x – x2 /2! + x3 /3! – x4 /4! + x5 /5! – x6 /6! (Input x)
#   d.	1+ x2 + x3 + x4 + x5 +…….. xn


# Code
from math import factorial

print("Series: 1+2+3+…….+n")
sum = 0
for x in range(1,int(input("n:\n"))+1): sum += x
print("Answer:",sum)

print("Series: 1^2+2^2+3^2+…..+n^2")
sum = 0
for x in range(1, int(input("n:\n"))+1): sum += x ** 2
print("Answer:",sum)

print("Series: x – x2 /2! + x3 /3! – x4 /4! + x5 /5! – x6 /6! (Input x) ")
sum = 0
x = int(input("x:\n"))
for n in range(1,7): sum += ( (x ** n) / (factorial(n)) ) * ((-1) ** (n-1) )# ; print(( (x ** n) / (factorial(n)) ) * ((-1) ** (n-1) )) print each part in order to verify if it is correct
print("Answer:",sum)

print("Series: 1+ x2 + x3 + x4 + x5 +…….. xn")
sum, x, n, = 0, int(input("x:\n"),), int(input("n:\n"))
for d in range(n+1): sum += x**d
print("Answer:",sum)
# Input
#   Series: 1+2+3+…….+n
#   n:
#   2
#   Answer: 3
#   Series: 1^2+2^2+3^2+…..+n^2
#   n:
#   2
#   Answer: 5
#   Series: x – x2 /2! + x3 /3! – x4 /4! + x5 /5! – x6 /6! (Input x)
#   x:
#   3
#   Answer: 0.6375
#   Series: 1+ x2 + x3 + x4 + x5 +…….. xn
#   x:
#   3
#   n:
#   2
#   Answer: 13


# Additional Comments