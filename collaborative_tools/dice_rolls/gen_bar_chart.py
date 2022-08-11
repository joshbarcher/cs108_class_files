import matplotlib.pyplot as plt

mapRolls = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

# calculate frequencies
numRolls = 100
with open(f"{numRolls}_rolls.txt", "r") as reader:
    rolls = reader.readlines()

    for roll in rolls:
        roll = int(roll.strip())
        mapRolls[roll] += 1

# generate bar chart
plt.bar(mapRolls.keys(), mapRolls.values())
plt.title(f"{numRolls} Rolls")
plt.xlabel("Dice Sides")
plt.ylabel("Number of Rolls")
plt.show()

# generate pie chart
plt.pie(mapRolls.values(), labels=mapRolls.keys(), autopct='%.1f%%')
plt.title(f"{numRolls} Rolls")
plt.show()

# generate scatter plot
plt.scatter(mapRolls.keys(), mapRolls.values())
plt.title(f"{numRolls} Rolls")
plt.xlabel("Dice Sides")
plt.ylabel("Number of Rolls")
plt.show()

