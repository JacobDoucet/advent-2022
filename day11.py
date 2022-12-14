import re

data = open("day11.txt").read().split("\n")

operation_pattern = "= old (\*|\+) ([a-z0-9]+)"
test_pattern = "divisible by ([0-9]+)"
throw_to_pattern = "throw to (monkey [0-9]+)"

monkeys = []
currentMonkey = dict()

for line in data:
    if line.strip() == "":
        monkeys.append(currentMonkey)
        currentMonkey = dict()
        continue
    [key, val] = line.split(":")
    if bool(val):
        currentMonkey[key.strip()] = val.strip()
    else:
        currentMonkey["name"] = key.strip().lower()

if bool(currentMonkey):
    monkeys.append(currentMonkey)

plus_num = lambda num: lambda old: old + int(num)
times_num = lambda num: lambda old: old * int(num)
plus_old = lambda old: old + old
times_old = lambda old: old * old

def parse_op(m):
    op = re.search(operation_pattern, m["Operation"])
    if op.group(1) == "+" and op.group(2).isnumeric():
        return plus_num(op.group(2))
    if op.group(1) == "*" and op.group(2).isnumeric():
        return times_num(op.group(2))
    if op.group(1) == "+":
        return plus_old
    if op.group(1) == "*":
        return times_old

def inspection_round(monkey_lookup, div_worry_level, mod):
    for m in monkeys:
        name = m["name"]
        monkey = monkey_lookup[name]
        true_throw_to = re.search(throw_to_pattern, monkey["If true"]).group(1)
        false_throw_to = re.search(throw_to_pattern, monkey["If false"]).group(1)
        for (i, item) in enumerate(monkey["items"]):
            new_val = monkey["op"](item) % mod
            if div_worry_level > 1:
                new_val = int(new_val / div_worry_level)
            if new_val % monkey["mod"] == 0:
                monkey_lookup[true_throw_to]["items"].append(new_val)
            else:
                monkey_lookup[false_throw_to]["items"].append(new_val)
        monkey["inspections"] += len(monkey["items"])
        monkey["items"] = []

def do_inspections(rounds, div_worry_level):
    monkey_lookup = dict()
    mod = 1

    for monkey in monkeys:
        monkey["items"] = list(map(int, monkey["Starting items"].split(",")))
        monkey["op"] = parse_op(monkey)
        monkey["inspections"] = 0
        monkey["mod"] = int(re.search(test_pattern, monkey["Test"]).group(1))
        mod *= monkey["mod"]
        monkey_lookup[monkey["name"]] = monkey

    for r in range(0, rounds):
        inspection_round(monkey_lookup, div_worry_level, mod)

    top = [0] * 2
    for name in monkey_lookup:
        monkey = monkey_lookup[name]
        if monkey["inspections"] > top[0]:
            top[1] = top[0]
            top[0] = monkey["inspections"]
        elif monkey["inspections"] > top[1]:
            top[1] = monkey["inspections"]
    return top

top = do_inspections(20, 3)
print("Part 1:", top[0] * top[1])

top = do_inspections(10000, 1)
print("Part 2:", top[0] * top[1])