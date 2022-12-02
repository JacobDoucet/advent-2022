import sys

elves = open("day1.txt").read().split("\n\n")
n = int(sys.argv[1])

topCals = [0] * n

# Iterate through each elf's calories
for calories in [sum(map(int, elf.split("\n"))) for elf in elves]:
    # Iterate the topCals list
    for i, c in enumerate(topCals):
        # Sorted slice of top n cals
        if calories > topCals[i]:
            # Push current top cals down the slice to make room for a new topCal
            for j in range(len(topCals) - i - 1):
                i1 = len(topCals) - j - 2
                i2 = len(topCals) - j - 1
                topCals[i2] = topCals[i1]
            # The current calories belong in position i
            topCals[i] = calories
            break

print("Top", n, "Calories:", topCals)
print("Total:", sum(topCals))
