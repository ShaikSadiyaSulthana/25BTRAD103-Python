
# Dice Simulator Using Random Module

import random

num_dice = int(input("Enter number of dice: "))
num_rolls = int(input("Enter number of rolls: "))

for i in range(num_rolls):

    print("\nRoll", i + 1)

    results = []

    for j in range(num_dice):
        dice = random.randint(1, 6)
        results.append(dice)

    print("Dice Results:", results)
    print("Total:", sum(results))

print("\nDice simulation completed!")
