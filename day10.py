import re
import functools

data = open("day10.txt").read().split("\n")

pattern = "addx (-?[0-9]+)"
cycle = 0
x = 1

width = 40
height = 6

x_vals = dict()
screen = [""] * height

def record():
    x_vals.update({cycle: x})
    y = int((cycle - 1) / width)
    sprite = (cycle - 1) % width
    screen[y] += "#" if x in range(sprite - 1, sprite + 2) else " "

get_sum = lambda cycles: functools.reduce(lambda sum, next: sum + x_vals[next] * next, cycles, 0)

for line in data:
    if line == "noop":
        cycle += 1
        record()
        continue
    cycle += 1
    record()
    cycle += 1
    record()
    x += int(re.search(pattern, line).group(1))

print("Part 1:", get_sum([20, 60, 100, 140, 180, 220]))

print("Part 2:")
for row in screen:
    print(row)
