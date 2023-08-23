# problem  day 5
"""
chef and chefina are playing with dice in one turn,
both of them roll their dice at once.
atahey concider a turn to be good if the
sum of the numbers o theire dice is greater than 6 .
Given that in particular turn cheif and chefina got x and y
on their respective dice, find whether the turn was good.
"""
#example
"""
if chef rolls a 3 (x=3) and chefina rolls a 2 (y=2)
then the sum is 3+2=5 which is less than 6, thus the turn is not good.
The sum of numbers on the dice is x=3 y=4  3+4=7 which is greater than 6 .
thus the turn is good.
"""


def is_good_turn(x, y):
    # Calculate the sum of the dice values
    total_sum = x + y
    
    # Check if the sum is greater than 6
    if total_sum > 6:
        return "Good"
    else:
        return "Not Good"

# Test cases
x = int(input("Enter Chef's dice value: "))
y = int(input("Enter Chefina's dice value: "))
result = is_good_turn(x, y)
print("Turn is:", result)



"""
import random

def generate_random_dice_values():
    return [random.randint(1, 6), random.randint(1, 6)]

dice_values = generate_random_dice_values()
print("Chef's dice value:", dice_values[0])
print("Chefina's dice value:", dice_values[1])

total_sum = sum(dice_values)
if total_sum > 6:
    print("Turn is Good")
else:
    print("Turn is Not Good")
"""








