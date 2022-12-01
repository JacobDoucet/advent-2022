import sys

elves = open("day1.txt").read().split("\n\n")

num = int(sys.argv[1])

cals = [0] * num

for calories in [sum(map(int, elf.split("\n"))) for elf in elves]:
    for i, c in enumerate(cals):
        if calories > cals[i]:
            for j in range(len(cals) - i - 1):
                if cals[len(cals) - j - 2] > cals[len(cals) - j - 1]:
                    cals[len(cals) - j - 1] = cals[len(cals) - j - 2]
            cals[i] = calories
            break

print("Top", num, "Calories:", cals)
print("Total:", sum(cals))
