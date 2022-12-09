import re

def move_head(pos, vector):
    return [pos[0] + vector[0], pos[1] + vector[1]]

def move_tail(next_head_pos, cur_tail_pos):
    delta = [ cur_tail_pos[0] - next_head_pos[0], cur_tail_pos[1] - next_head_pos[1] ]
    if abs(delta[0]) == 2 or abs(delta[1]) == 2:
        return [ next_head_pos[0] + int(delta[0] / 2), next_head_pos[1] + int(delta[1] / 2)]
    return cur_tail_pos

data = open("day9.txt").read()
pattern = "(?:([A-Z]) ([0-9]+))"
vectors = list(map(lambda match: {"dir": match[0], "delta": int(match[1])}, re.findall(pattern, data)))
unit_vector = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}

def move_rope(n_knots):
    pos = []
    for _ in range(0, n_knots):
        pos.append([0, 0])
    tail = set()

    add_tail_pos = lambda p: tail.add(str(p[0]) + ":" + str(p[1]))

    for vector in vectors:
        for _ in range(0, vector["delta"]):
            pos[0] = move_head(pos[0], unit_vector[vector["dir"]])
            for i in range(1, n_knots):
                pos[i] = move_tail(pos[i - 1], pos[i])
            add_tail_pos(pos[n_knots - 1])
    return len(tail)


print("Part 1:", move_rope(2))
print("Part 2:", move_rope(10))
