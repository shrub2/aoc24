
with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        lines.append(line)

# Just in case
del line

result = 0

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char != 'X':
            continue

        #Horizontal checking

        left_to_right = line[char_index:char_index+4]

        if left_to_right == "XMAS":
            result += 1

        if char_index <= 3:
            right_to_left = line[char_index::-1]
        else:
            right_to_left = line[char_index:char_index-4:-1]

        if right_to_left == "XMAS":
            result += 1

        #Vertical checking

        vertical_top = ""
        for j in range(4):
            if line_index+j >= 0 and line_index+j < len(lines):
                vertical_top += lines[line_index+j][char_index]
        if vertical_top == "XMAS":
            result += 1

        vertical_bot = ""
        for j in range(4):
            if line_index-j >= 0 and line_index-j < len(lines):
                vertical_bot += lines[line_index-j][char_index]
        if vertical_bot == "XMAS":
            result += 1

        #Diagonal checking

        diagonal_top_left = ""
        for j in range(4):
            if line_index+j >= 0 and line_index+j < len(lines) and char_index+j >= 0 and char_index+j < len(line):
                diagonal_top_left += lines[line_index+j][char_index+j]
        if diagonal_top_left == "XMAS":
            result += 1
    
        diagonal_top_right = ""
        for j in range(4):
            if line_index+j >= 0 and line_index+j < len(lines) and char_index-j >= 0 and char_index-j < len(line):
                diagonal_top_right += lines[line_index+j][char_index-j]
        if diagonal_top_right == "XMAS":
            result += 1

        diagonal_bot_left = ""
        for j in range(4):
            if line_index-j >= 0 and line_index-j < len(lines) and char_index+j >= 0 and char_index+j < len(line):
                diagonal_bot_left += lines[line_index-j][char_index+j]
        if diagonal_bot_left == "XMAS":
            result += 1

        diagonal_bot_right = ""
        for j in range(4):
            if line_index-j >= 0 and line_index-j < len(lines) and char_index-j >= 0 and char_index-j < len(line):
                diagonal_bot_right += lines[line_index-j][char_index-j]
        if diagonal_bot_right == "XMAS":
            result += 1


print(result)
