
with open('input.txt', 'r') as file:
    cells = []
    for index, line in enumerate(file):
        cells.append([])
        for character in line.strip():
            cells[index].append(character) 

def get_guard_coords(cells):
    for y, line in enumerate(cells):
        for x, char in enumerate(line):
            if set(["^", ">", "V", "<"]) & set(char):
                return y, x, char

y, x, char = get_guard_coords(cells)
y_bounds, x_bounds = len(cells), len(cells[0])

while(True):
    # Move up
    if char == "^":
        if y-1 < 0:
            cells[y][x] = "X"
            break
        if cells[y-1][x] == "#":
            cells[y][x] = ">"
            char = ">"
        else:
            cells[y-1][x] = "^"
            cells[y][x] = "X"
            y -= 1
    
    # Move right
    if char == ">":
        if x+1 >= x_bounds:
            cells[y][x] = "X"
            break
        if cells[y][x+1] == "#":
            cells[y][x] = "V"
            char = "V"
        else:
            cells[y][x+1] = ">"
            cells[y][x] = "X"
            x += 1

    # Move down
    if char == "V":
        if y+1 >= y_bounds:
            cells[y][x] = "X"
            break
        if cells[y+1][x] == "#":
            cells[y][x] = "<"
            char = "<"
        else:
            cells[y+1][x] = "V"
            cells[y][x] = "X"
            y += 1

    # Move down
    if char == "<":
        if x-1 < 0:
            cells[y][x] = "X"
            break
        if cells[y][x-1] == "#":
            cells[y][x] = "^"
            char = "^"
        else:
            cells[y][x-1] = "<"
            cells[y][x] = "X"
            x -= 1


result = 0
for cell in cells:
    for char in cell:
        if char == "X":
            result += 1

print(result)
