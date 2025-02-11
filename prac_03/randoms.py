import random

print(random.randint(5, 20))  # line 1
# Line 1: output a random integer between 5 (inclusive) and 20 (inclusive)
# The smallest possible output is 5, and the largest possible output is 20

print(random.randrange(3, 10, 2))  # line 2
# Line 2: output a random number in [3, 5, 7, 9]
# The smallest possible output is 3, and the largest possible output is 9
# Not possible to output a 4

print(random.uniform(2.5, 5.5))  # line 3
# Line 3: output a random number from 2.5 (inclusive) to 5.5 (inclusive)
# The smallest possible output is 2.5, and the largest possible output is 5.5

print(random.uniform(1, 100)) # output a random number between 1 and 100 (inclusive)