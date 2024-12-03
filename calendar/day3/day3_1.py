import re

with open('input.txt', 'r') as file:
    program_memory = file.read()

pattern = r"mul\((\d+),(\d+)\)"

mul_list = re.findall(pattern, program_memory)

result = 0
for number1, number2 in mul_list:
    result += int(number1) * int(number2)

print(result)
