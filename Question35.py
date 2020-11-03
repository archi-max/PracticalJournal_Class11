# Question
# 35. Create a dictionary whose keys are month names and whose values are number of days in the      corresponding months. Perform the following:
# Ask the user to enter a month name ,and use dictionary to tell how many days are in the month.
# Print out all of the months with 31 days.
# Print out all of the keys in alphabetical order

# Code
months_l = ["january","february","march","april","may","june","july","august","september","october","november","december"]
months = {}
for x in range(len(months_l)):
    days = 0
    x += 1
    if x == 2: days = 27
    elif x <= 7:
        if x%2 == 0: days = 30
        else: days = 31
    else:
        if x%2 == 0: days = 31
        else: days = 30
    months[months_l[x-1]] = days


print("days in the month: ", months[input("month:\n").lower()])

print()
print("Months with 31 days:")
for item, value in months.items():
    if value == 31:
        print(item)

print("Sorted Months")
sm = list(months.keys())
sm.sort()
print(sm)

# Input
#   month:
#   january
#   days in the month:  31
#
#   Months with 31 days:
#   january
#   march
#   may
#   july
#   august
#   october
#   december
#   Sorted Months
#   ['april', 'august', 'december', 'february', 'january', 'july', 'june', 'march', 'may', 'november', 'october', 'september']

# Additional Comments
