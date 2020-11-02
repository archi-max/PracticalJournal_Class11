# question
# 20.	Write a program to count number of vowels in a given sentence.

#code

s = input('String:\n')
count = 0
for x in s:
    if x in ['a','e','i','o','u']:
        count += 1

print("No of vowels:",count)

# Input
#   String:
#   python
#   No of vowels: 1
