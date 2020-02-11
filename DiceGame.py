import random
from math import floor

die1 = 0
die2 = 0
dice_total = 0
avg_dice = 0

def dice_roll():
    rollOutput = random.randint(1, 6)
    return rollOutput


roll_count = int(input("Enter the amount of rolls you would like to throw\n"))


i = 0
while i < roll_count:
    die1 = dice_roll()
    die2 = dice_roll()
    diceTotal = die1 + die2
    avg_dice += diceTotal
    print('Die 1 value: ', die1)
    print('Die 2 value: ', die2)
    print('Total Dice Roll: ', diceTotal)
    i += 1


dice_average = floor((avg_dice/ roll_count))
print('Average: ', dice_average)
