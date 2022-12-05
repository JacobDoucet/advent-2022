import re

data = open('day5.txt').read()

def groups_of(list, parts):
    return [list[i:i + parts] for i in range(0, len(list), parts)]

[crates, instructions] = data.split("\n\n")

crates = crates.split("\n")
nums = crates.pop().split(" ")

def mover(reverse):
    # Initialize stacks
    stacks = []
    for n in nums:
        if n != "":
            stacks.append([])

    for line in crates:
        line = groups_of(line, 4)
        for i, cell in enumerate(line):
            if cell.strip() != "":
                stacks[i].append(cell)

    # Apply instructions
    reg = "move ([0-9]+) from ([0-9]+) to ([0-9]+)"
    for instruction in instructions.split("\n"):
        [[num, moveFrom, moveTo]] = re.findall(reg, instruction)
        num = int(num)
        moveFrom = int(moveFrom) - 1
        moveTo = int(moveTo) - 1
        items = stacks[moveFrom][0:num]

        if reverse:
            items.reverse()

        for item in items:
            stacks[moveTo].insert(0, item)
        del stacks[moveFrom][0:num]

    answer = ""
    for i, s in enumerate(stacks):
        answer += s[0]
    return re.sub(" |\[|\]", "", answer)

print("Part 1:", mover(False))
print("Part 2:", mover(True))
