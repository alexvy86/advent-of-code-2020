from utils import read_lines

grid = read_lines(3)
horizontal_wrap = len(grid[0])

num_rows = len(grid)

current_coords = (0,0)

horizontal_step = 3
vertical_step = 1

num_trees = 0

while(current_coords[0] < num_rows - 1):
	current_coords = (current_coords[0] + vertical_step, current_coords[1] + horizontal_step)
	if grid[current_coords[0]][current_coords[1] % horizontal_wrap] == "#":
		num_trees += 1

print(num_trees)
