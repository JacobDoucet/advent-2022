filename = "day8.txt"
data = list(map(lambda line: list(map(lambda n: int(n), line)), open(filename).read().split("\n")))

col_height = len(data)
row_width = len(data[0])
highest_score = -1
trees_visible = 0

for (y0, line) in enumerate(data):
    for (x0, h) in enumerate(line):

        xI = list(range(0, x0))
        xI.reverse()
        xN = range(x0 + 1, len(line))
        yI = list(range(0, y0))
        yI.reverse()
        yN = range(y0 + 1, len(data))

        score_parts = [0] * 4
        visible = False

        for xn in xI:
            if line[xn] >= line[x0]:
                score_parts[0] = x0 - xn
                break
        else:
            score_parts[0] = x0
            visible = True

        for xn in xN:
            if line[xn] >= line[x0]:
                score_parts[1] = xn - x0
                break
        else:
            score_parts[1] = row_width - x0 - 1
            visible = True

        for yn in yI:
            if data[yn][x0] >= data[y0][x0]:
                score_parts[2] = y0 - yn
                break
        else:
            score_parts[2] = y0
            visible = True

        for yn in yN:
            if data[yn][x0] >= data[y0][x0]:
                score_parts[3] = yn - y0
                break
        else:
            score_parts[3] = col_height - y0 - 1
            visible = True

        if visible:
            trees_visible += 1

        score = score_parts[0] * score_parts[1] * score_parts[2] * score_parts[3]
        if score > highest_score:
            highest_score = score

print("Part 1:", trees_visible)
print("Part 2:", highest_score)