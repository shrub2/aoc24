

with open('input.txt', 'r') as file:
    reports = []

    for line in file:
        levels = []
        for level in line.strip().split():
            levels.append(int(level))
        reports.append(levels)

safe_count = 0

for report in reports:
    decreasing = 1
    increasing = 1
    safe = 1

    for current_lvl, next_lvl in zip(report, report[1:]):

        if abs(current_lvl - next_lvl) > 3:
            safe = 0
            break

        if (current_lvl > next_lvl) and decreasing:
            increasing = 0
        elif (current_lvl < next_lvl) and increasing:
            decreasing = 0
        else:
            safe = 0
            break

    if safe:
        safe_count += 1

print(safe_count)
