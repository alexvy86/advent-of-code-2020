from utils import read_lines

grid = read_lines(3)
horizontal_wrap = len(grid[0])

num_rows = len(grid)

steps = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

product = 1
for s in steps:

    current_coords = (0, 0)
    num_trees = 0

    while(current_coords[0] < num_rows - 1):
        current_coords = (current_coords[0] + s[1], current_coords[1] + s[0])
        if grid[current_coords[0]][current_coords[1] % horizontal_wrap] == "#":
            num_trees += 1

    print(f"{s[0]},{s[1]} - {num_trees}")
    product *= num_trees

print(product)