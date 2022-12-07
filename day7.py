import re

# Part 1
max_size = 100000

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

total_size = 0
total_size_under_limit = 0
for path in filter(lambda p: folders[path] <= max_size, folders):
    total_size_under_limit += folders[path]

print("Part 1:", total_size_under_limit)

# Part 2

system_size = 70000000
required_unused_size = 30000000
system_max_used_size = system_size - required_unused_size

min_free_up_space = folders["/"] - system_max_used_size
# Start with the root folder. All child folders will be smaller
size_to_remove = folders["/"]
for path in folders:
    if min_free_up_space < folders[path] < size_to_remove:
        size_to_remove = folders[path]

print("Part 2:", size_to_remove)

