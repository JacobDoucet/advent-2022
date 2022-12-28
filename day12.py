a = ord("a")
diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

coord_key = lambda i, j: str(i) + "-" + str(j)
queue = []

def enqueue_step(i, j, grid, target, history, n):
    queue.append(lambda : take_step(i, j, grid, target, history, n))

def take_step(i, j, grid, target, history, n):
    # Generate coordinate key
    key = coord_key(i, j)
    # Check for previous visit in less steps
    if key in history and history[key] <= n:
        return
    # Arrived to current coordinate in the least amount of steps (so far)
    history[key] = n
    # Check for target
    if target[0] == i and target[1] == j:
        return
    # Move on to boundaries
    next_n = n + 1
    for [d_i, d_j] in diffs:
        i_n = i + d_i
        j_n = j + d_j
        # Make sure coord is within the grid
        if i_n < 0 or i_n >= len(grid) or j_n < 0 or j_n >= len(grid[i_n]):
            continue
        # Make sure we can take a step to the next coord
        if grid[i][j] >= grid[i_n][j_n] - 1:
            enqueue_step(i_n, j_n, grid, target, history, next_n)
            continue

def prepare(raw):
    grid = []
    s_coord = []
    a_coords = []
    e_coord = []
    for i, _ in enumerate(raw):
        line = []
        for j, _ in enumerate(raw[i]):
            if raw[i][j] == "S":
                line.append(ord("a"))
                s_coord = [i, j]
                a_coords.append([i, j])
                continue
            if raw[i][j] == "E":
                line.append(ord("z"))
                e_coord = [i, j]
                continue
            if raw[i][j] == "a":
                a_coords.append([i, j])
            line.append(ord(raw[i][j]))
        grid.append(line)
    return grid, s_coord, a_coords, e_coord

def init_queue(grid, start_coords, target):
    history = dict()
    for [i, j] in start_coords:
        enqueue_step(i, j, grid, target, history, 0)
    return history

def process_queue():
    while len(queue) > 0:
        next = queue.pop(0)
        next()

g, s_coord, a_coords, e_coord = prepare(open("day12.txt").read().split("\n"))
e_key = coord_key(e_coord[0], e_coord[1])

h = init_queue(g, [s_coord], e_coord)
process_queue()
print("Part 1:", h[e_key])

h = init_queue(g, a_coords, e_coord)
process_queue()
print("Part 2:", h[e_key])
