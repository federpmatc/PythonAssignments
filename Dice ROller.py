https://youtu.be/x-Ag2_bJ40Y?si=p75xbLVg_K6YgwKg

import random

#dictionaries are key/value pairs
#dice_art is a dictionary where the keys are the numbers on the dice (1-6)
#and the values are collections representing the visual representation of each die face

dice_art = {
    1: ["┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"],
    2: ["┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"],
    3: ["┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"],
    4: ["┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"],
    5: ["┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"],
    6: ["┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"]
}
di1 = dice_art.get(1)
print(di1)

print(di1[0])  # Example of accessing the top line of the die face for 1
print(di1[1])  # Example of accessing the top line of the die face for 1
print(di1[2])  # Example of accessing the top line of the die face for 1
print(di1[3])  # Example of accessing the top line of the die face for 1
print(di1[4])  # Example of accessing the top line of the die face for 1

di1 = dice_art.get(1)
for line in di1:
    print(line)

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))


#PRINT VERTICALLY
for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

#PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")