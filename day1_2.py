elves = open("day1.txt").read().split("\n\n")

cal1 = 0
cal2 = 0
cal3 = 0
for i in elves:
    items = i.split("\n")
    calories = 0
    for j in items:
        calories += int(j)

    if calories > cal1:
        if cal1 > cal2:
            if cal2 > cal3:
                cal3 = cal2
            cal2 = cal1
        cal1 = calories
        continue
    if calories > cal2:
        if cal2 > cal3:
            cal3 = cal2
        cal2 = calories
        continue
    if calories > cal3:
        cal3 = calories

print(cal1 + cal2 + cal3)
