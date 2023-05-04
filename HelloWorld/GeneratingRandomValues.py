# Importing external module built into python
import random

#3 random values between 0 and 1
for i in range(3):
    print(random.random())

# 3 random values between 10 and 20
for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


class Dice:
    # def __init__(self, possible_rolls):
    #     self.possible_rolls = (1,2,3,4,5,6)

    def roll(self):
        first = (random.randint(1,6))
        second = (random.randint(1,6))
        return (first, second)


dice = Dice()
print(dice.roll())
