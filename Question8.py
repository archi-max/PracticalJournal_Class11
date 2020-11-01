# Question:

# Write a program to find the roots of the quadratic equation.

# Code:



eq = input("Quadratic equation in form of ax^2 + bx + c:\n")
a = 0
b = 0
c = 0



#try to get correct equation
while eq.find("x^2") == -1:
    eq = input("Please enter correct quadratic equation(x^2 not found):\n")
else:
    for _ in range(eq.count("x^2")):
        tmp_a = ''
        tmp = ''  # record character being processed
        for x in eq[:eq.find("x^2")][
                 ::-1]:  # [len(eq) - eq.find("x^2"):]: #basically loop all characters before x^2 in reverse direction
            tmp += x
            if x == " ": continue
            # print(x, end="")
            tmp_a += x
            if x == "+" or x == "-": break
        # eq = eq.replace('x^2', '')
        tmp = tmp[::-1]
        eq = eq.replace(tmp + 'x^2', '', 1)  # remove processed characters
        if tmp_a.strip()[::-1] not in ['','+','-']:
            a += int(tmp_a[::-1])
        else:
            a += int(tmp_a[::-1]+'1')
    print("a:", a)
print("eq:",eq)

#try to get correct equation as no proper x value found. NOTE: this assumes that a won't change
while eq.find("x") == -1:
    eq = input("Please enter correct quadratic equation. x not found:\n")
else:
    for _ in range(eq.count("x")):
        tmp = ''
        tmp_b = ''
        for x in eq[:eq.find("x")][::-1]:  # [len(eq) - eq.find("x"):]:
            tmp += x
            if x == " ": continue
            tmp_b += x
            if x == "+" or x == "-": break
        # eq = eq.replace('x', '')
        tmp = tmp[::-1]
        print("tmpx", tmp + 'x')
        eq = eq.replace(tmp + 'x', '')
        if tmp_b.strip()[::-1] not in ['','+','-']:
            # print("b:", tmp_b[::-1])
            b += int(tmp_b[::-1])
        else:
            b += int(tmp_b[::-1] + '1')
    print("b:", b)

print("eq:",eq)
# eq = eq.replace("+","")
eq = eq.replace(" ","")


try:
    c = eval(eq)
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