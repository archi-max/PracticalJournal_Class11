# Question:

# Write a program to find the roots of the quadratic equation.

# Code:



eq = input("Quadratic equation in form of ax^2 + bx + c:\n")
a = ''
b = ''
c = ''



#try to get correct equation
while eq.find("x^2") == -1:
    eq = input("Please enter correct quadratic equation(x^2 not found):\n")
else:
    tmp = '' #record character being processed
    for x in eq[:eq.find("x^2")][::-1]:#[len(eq) - eq.find("x^2"):]: #basically loop all characters before x^2 in reverse direction
        tmp += x
        if x == " ": continue
        # print(x, end="")
        a += x
        if x == "+" or x == "-": break
    # eq = eq.replace('x^2', '')
    tmp = tmp[::-1]
    eq = eq.replace(tmp+'x^2','') #remove processed characters
    if a != '':
        a = int(a[::-1])
    else:
        a = 1
    print("a:",a)
print("eq:",eq)

#try to get correct equation as no proper x value found. NOTE: this assumes that a won't change
while eq.find("x") == -1:
    eq = input("Please enter correct quadratic equation. x not found:\n")
else:
    tmp = ''
    for x in eq[:eq.find("x")][::-1]:#[len(eq) - eq.find("x"):]:
        tmp += x
        if x == " ": continue
        b += x
        if x == "+" or x == "-": break
    # eq = eq.replace('x', '')
    tmp = tmp[::-1]
    print("tmpx",tmp+'x')
    eq = eq.replace(tmp+'x', '')
    if b != '':
        print("b:", b[::-1])
        b = int(b[::-1])
    else:
        b = 1
    print("b:",b)

print("eq:",eq)
# eq = eq.replace("+","")
eq = eq.replace(" ","")


try:
    c = int(eq)
    print("c:",c)
except:
    print("invalid equation!")

det = (b**2) - (4 * a * c) # determinant
print("det:",det)
if det == 0:
    print("Equal roots")
    root = ((-1*b) + (det**1/2))/ (2 * a)
    print("root:",root)
elif det < 0:
    print("no real roots")
else:
    print("2 roots")
    root1 = ((-1 * b) + (det ** 1 / 2)) / (2 * a)
    root2 = ((-1 * b) - (det ** 1 / 2)) / (2 * a)
    print("roots:",root1,",",root2)


# Output:

#    Quadratic equation in form of ax^2 + bx + c:
#    2x^2 - 2x + 0
#    a: 2
#    eq:  - 2x + 0
#    tmpx - 2x
#    b: -2
#    b: -2
#    eq:   + 0
#    c: 0
#    det: 4
#    2 roots
#    roots: 1.0 , 0.0