
with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        lines.append(line)

# Just in case
del line

match = "MAS"
result = 0

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):

        diag_top_left = ""
        for j in range(len(match)):
            char_jndex = char_index+j
            line_jndex = line_index+j
            if line_jndex >= 0 and line_jndex < len(lines) and char_jndex >= 0 and char_jndex < len(line):
                diag_top_left += lines[line_jndex][char_jndex]

        diag_bot_left = ""
        for j in reversed(range(len(match))):
            char_jndex = char_index+len(match)-1-j
            line_jndex = line_index+j
            if line_jndex >= 0 and line_jndex < len(lines) and char_jndex >= 0 and char_jndex < len(line):
                diag_bot_left += lines[line_jndex][char_jndex]

        if (diag_top_left == match or diag_top_left == match[::-1]) and (diag_bot_left == match or diag_bot_left == match[::-1]):
            result += 1


print(result)
