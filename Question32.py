# Question
# 32.	Write  a	program	to	perform	various   list	operations	using	menu	driven operations.
# a.	Add element	c. Delete element	          e. Display list
# b.	Modify element	d. Add another list	f. Exit

# Code
import string

actions = ["Add element", "Delete element", "Display list",
           "Modify element", "Add another list", "Exit"
           ]

ml = []

while True:
    for i, action in enumerate(actions):
        actions[i] = action.lower()
    title = "List Operator"

    print("-" * len(title))
    print(title)
    print("-" * len(title))
    print()
    # print("current list:", ml)
    print()
    print("Operations:")

    for i, action in enumerate(actions): print(string.ascii_letters[i], ":", action)

    a = input("\n")
    while string.ascii_letters.index(a.lower()) > len(actions):
        a = input("Please enter from the given options:\n")
    to_do_action = actions[string.ascii_letters.index(a.lower())]
    print()
    if to_do_action == 'add element':
        ml.append(input("element:\n"))
    elif to_do_action == 'delete element':
        del ml[int(input("Please enter the index of the element to delete:\n"))] # TODO: Add a try and error condition in case entered number is not in the range of list
    elif to_do_action == 'display list':
        print(ml)
    elif to_do_action == 'modify element':
        i = int(input("Please enter the index of the element to modify:\n"))
        ml[i] = input("The new element:\n")

    elif to_do_action == 'add another list':
        i = input("Please enter the elements seperated by comma\n")
        for x in i.split(","): ml.append(x.strip())
    elif to_do_action == 'exit':
        print(
            "Goodbye! Hopefully I was a good list operator") # The guy in black robes says yes u were a good operator! Only redditors will understand :D
        break
    print()
# Input
# Too big.

# Additional Comments
