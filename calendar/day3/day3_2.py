import re

with open('input.txt', 'r') as file:
    program_memory = file.read()

patterns = {
    "mul": r"mul\((\d+),(\d+)\)",
    "do": r"do\(\)",
    "dont": r"don't\(\)"
}

matches = []
for action, pattern in patterns.items():
    for match in re.finditer(pattern, program_memory):
        matches.append((match.start(), match, action))

matches.sort(key=lambda x: x[0])

multiply = True
result = 0

for _, match, action in matches:
    if action == "mul" and multiply:
        mul_tuple = match.groups()
        result += int(mul_tuple[0]) * int(mul_tuple[1])
    elif action == "do":
        multiply = True
    elif action == "dont":
        multiply = False


print(result)
