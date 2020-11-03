# Question
#   34.	Write a program to repeatedly ask user to enter a team name and now many games the team has won or last.
#       c. Using dictionary, allow the user to enter team name and print out the team’s win percentage.
#       d. Using it to create a list whose entries are the number of runs of each team.
#       e. Using dictionary create a list of all teams having winning records.

# Code
t = {}
while True:
    a = input("Team name, wins, looses seprated by commas. Press n to finish entering!:\n")
    if a == "n" or a.replace(" ","").strip() == "": break
    al = [i.strip() for i in a.split(",")]
    t[al[0]] = {"wins":int(al[1]),"looses":int(al[2])}

for key, value in t.items():
    print(key+'\'s win precentage:', "{}%".format((value["wins"]/(value["wins"]+value["looses"]))*100))
print()
runs = []
for key in t.keys(): runs.append(int(input(key+'\'s runs:\n')))

print(runs)
print()

wins = {}
for key, value in t.items():
    wins[key] = value["wins"]
print("wins:",wins)
# Input
#   Team name, wins, looses seprated by commas. Press n to finish entering!:
#   sdqwedqd, 3, 1
#   Team name, wins, looses seprated by commas. Press n to finish entering!:
#   wedwedw, 2, 1
#   Team name, wins, looses seprated by commas. Press n to finish entering!:
#   qedqdwd, 1, 5
#   Team name, wins, looses seprated by commas. Press n to finish entering!:
#   qwdqwd, 6, 0
#   Team name, wins, looses seprated by commas. Press n to finish entering!:
#   efweffwe, 3, 3
#   Team name, wins, looses seprated by commas. Press n to finish entering!:
#
#   sdqwedqd's win precentage: 75.0%
#   wedwedw's win precentage: 66.66666666666666%
#   qedqdwd's win precentage: 16.666666666666664%
#   qwdqwd's win precentage: 100.0%
#   efweffwe's win precentage: 50.0%
#
#   sdqwedqd's runs:
#   3
#   wedwedw's runs:
#   4
#   qedqdwd's runs:
#   5
#   qwdqwd's runs:
#   6
#   efweffwe's runs:
#   1
#   [3, 4, 5, 6, 1]
#
#   {'sdqwedqd': 3, 'wedwedw': 2, 'qedqdwd': 1, 'qwdqwd': 6, 'efweffwe': 3}

# Additional Comments
