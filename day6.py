chars = open("day6.txt").read()

def detect_message(size):
    for (i, char) in enumerate(chars):
        if len(set(chars[i:(i+size)])) == size:
            return i + size

print("Part 1:", detect_message(4))
print("Part 2:", detect_message(14))
