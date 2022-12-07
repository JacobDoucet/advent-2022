import re

data = open("day7.txt").read().split("\n")

navigate_down = "cd ([A-Za-z0-9]+)"
navigate_up = "cd \.\."
file_size = "([0-9]+) (?:[A-Za-z0-9]+)"

folders = dict()
current_dir = [""]

for row in data:
    if re.search(navigate_up, row):
        current_dir.pop()
    elif re.search(navigate_down, row):
        current_dir.append(re.findall(navigate_down, row)[0])
    elif re.search(file_size, row):
        next_size = int(re.findall(file_size, row)[0])
        path = ""
        for dir in current_dir:
            path += "/" + dir
            if not path in folders:
                folders[path] = 0
            folders[path] += next_size

# Part 1

max_size = 100000
total_size = 0
print("Part 1:", sum(filter(lambda size: size <= max_size, map(lambda path: folders[path], folders))))

# Part 2

system_size = 70000000
required_unused_size = 30000000
system_max_used_size = system_size - required_unused_size
min_free_up_space = folders["/"] - system_max_used_size
print("Part 2:", min(list(filter(lambda size: min_free_up_space < size, map(lambda path: folders[path], folders)))))
