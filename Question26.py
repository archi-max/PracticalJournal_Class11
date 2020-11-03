# Question
# Ask the user to enter a list of strings. Create a new list that contains only those strings which start with a vowel.

# Code

x = []
y = []
while True:
    print("String",str(len(x)+1)+ ':')
    i = input()
    if i != '!':
        x.append(i)
    else: break

for e in x: y.append(e) if e[0] in 'aeiou' else None
print("New list:",y)
# Input
#   String 1:
#   wrwrg
#   String 2:
#   efgfd
#   String 3:
#   aefe
#   String 4:
#   hrtetg
#   String 5:
#   qertrt
#   String 6:
#   oijrw
#   String 7:
#   !
#   New list: ['efgfd', 'aefe', 'oijrw']

# Additional Comments