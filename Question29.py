# Question
# 29.	Write a program to create a nested tuple to store marks of three subjects for five students. Compute the total marks and average obtained by each student.

# Code
marks = (
    (80, 79, 65),
    (76, 72, 70),
    (78, 77, 69),
    (71, 79, 73),
    (68, 72, 76),
)

for i, x in enumerate(marks):
    print(f"Total marks for subject {i + 1}:",sum(x))
    print(f"Average marks for subject {i + 1}:", sum(x)/len(x))

# Input
#   Total marks for subject 1: 224
#   Average marks for subject 1: 74.66666666666667
#   Total marks for subject 2: 218
#   Average marks for subject 2: 72.66666666666667
#   Total marks for subject 3: 224
#   Average marks for subject 3: 74.66666666666667
#   Total marks for subject 4: 223
#   Average marks for subject 4: 74.33333333333333
#   Total marks for subject 5: 216
#   Average marks for subject 5: 72.0

# Additional Comments
