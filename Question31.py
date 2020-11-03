# Question
# 31.	Given  a  tuple  pairs  =  {(2,5),(4,2),(9,8),(12,10)}  ,  count  the  number  of  pairs  (a,b) such that both a and b are even.

# Code

tp = {(2,5),(4,2),(9,8),(12,10)}
nl = []

for tup in tp: nl.append(tup) if (tup[0]%2==0 and tup[1]%2==0) else None
print(nl)

# Input


# Additional Comments
