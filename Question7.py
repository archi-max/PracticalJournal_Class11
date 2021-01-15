# Question:-

# WAP to generate 6 random numbers between 100 and 999 and then print their mean, median and mode

# CODE:-

# For this one, we gotta import random module (it is used to generate random numbers).
# Also added the statistics module for finding mean , median and mode
import random
import statistics

# Now, we will put our range in a variable so as to make it more easy to use.
# Notice that the question says b/w 100 and 999 i.e. these can't be included. So I had to put 101 as lower limit and since upper limit is not counted, I left it as 999.
given_range=range(101,999)

# Now, we have to use random.choices() method as we are trying to pick 6 numbers at random from given range.
# Also. we have to specify a value 'k' which tells how many times do we want a random number; in this case k=6.
# We can assign it a variable for easy use.
nums=random.choices(given_range,k=6)

# Finding the mode
print("mode",statistics.mode(nums))
# Finding the mean
print("mean",statistics.mean(nums))
# Finding the median
print("median",statistics.median(nums))

# No additional comments



