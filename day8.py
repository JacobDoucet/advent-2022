import math

filename = "day8.txt"
data = list(map(lambda line: list(map(lambda n: int(n), line)), open(filename).read().split("\n")))

height = len(data)
width = len(data[0])
highestScore = -1
treesVisible = 0

for y0, _ in enumerate(data):
    for x0, _ in enumerate(data[y0]):

        # Check to the left
        xLeft = list(range(0, x0))
        xLeft.reverse()
        # Check to the right
        xRight = range(x0 + 1, width)
        # Check above
        yAbove = list(range(0, y0))
        yAbove.reverse()
        # Check below
        yBelow = range(y0 + 1, height)

        score = 1
        visible = False

        for xn in xLeft:
            if data[y0][xn] >= data[y0][x0]:
                score *= x0 - xn
                break
        else:
            score *= x0
            visible = True

        for xn in xRight:
            if data[y0][xn] >= data[y0][x0]:
                score *= xn - x0
                break
        else:
            score *= width - x0 - 1
            visible = True

        for yn in yAbove:
            if data[yn][x0] >= data[y0][x0]:
                score *= y0 - yn
                break
        else:
            score *= y0
            visible = True

        for yn in yBelow:
            if data[yn][x0] >= data[y0][x0]:
                score *= yn - y0
                break
        else:
            score *= height - y0 - 1
            visible = True

        if visible:
            treesVisible += 1

        if score > highestScore:
            highestScore = score

print("Part 1:", treesVisible)
print("Part 2:", highestScore)
