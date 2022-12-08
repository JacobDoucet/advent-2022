import math

filename = "day8.txt"
data = list(map(lambda line: list(map(lambda n: int(n), line)), open(filename).read().split("\n")))

height = len(data)
width = len(data[0])
highestScore = -1
treesVisible = 0

for y0, _ in enumerate(data):
    for x0, _ in enumerate(data[y0]):

        score = 1
        visible = False

        # Left
        for X in reversed(list(range(0, x0))):
            if data[y0][X] >= data[y0][x0]:
                score *= x0 - X
                break
        else:
            score *= x0
            visible = True

        # Right
        for X in range(x0 + 1, width):
            if data[y0][X] >= data[y0][x0]:
                score *= X - x0
                break
        else:
            score *= width - x0 - 1
            visible = True

        # Above
        for Y in reversed(list(range(0, y0))):
            if data[Y][x0] >= data[y0][x0]:
                score *= y0 - Y
                break
        else:
            score *= y0
            visible = True

        # Below
        for Y in range(y0 + 1, height):
            if data[Y][x0] >= data[y0][x0]:
                score *= Y - y0
                break
        else:
            score *= height - y0 - 1
            visible = True

        treesVisible += 1 if visible else 0
        highestScore = score if score > highestScore else highestScore

print("Part 1:", treesVisible)
print("Part 2:", highestScore)
