# Which Elf is carrying the most calories?

lines = open("day1.txt").read().split("\n")

current = 0
largest = 0
for i in lines:
    if i == "":
        if current > largest:
            largest = current
        current = 0
    else:
        current += int(i)

if current > largest:
    largest = current

print(largest)