import random

# roll dice n times
times = 5
fileName = f"{times}_rolls.txt"

with open(fileName, "w") as writer:
    for i in range(times):
        roll = random.randint(1, 6)
        writer.write(f"{roll}\n")
