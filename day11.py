from utils import read_lines

neighbor_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def read_grid_from_file():
	grid = [list(f".{row}.") for row in read_lines(11)]
	grid = [list("." * len(grid[0]))] + grid + [list("." * len(grid[0]))]
	return grid

def update_state(grid):
	original_grid = [r.copy() for r in grid]
	changes_occurred = False
	for row in range(1,len(grid) - 1):
		for col in range(1, len(grid[0]) - 1):
			adjacent_occupied_seats = "".join(original_grid[row + r][col + c] for (r, c) in neighbor_coords).count("#")
			if original_grid[row][col] == "L" and adjacent_occupied_seats == 0:
				grid[row][col] = "#"
				changes_occurred = True
			elif original_grid[row][col] == "#" and adjacent_occupied_seats >= 4:
				grid[row][col] = "L"
				changes_occurred = True
	return changes_occurred

def update_state_v2(grid):
	original_grid = [r.copy() for r in grid]
	changes_occurred = False
	for row in range(1,len(grid) - 1):
		for col in range(1, len(grid[0]) - 1):
			visible_occupied_seats = 0
			for (r, c) in neighbor_coords:
				current_cell = (row + r, col + c)
				while current_cell[0] >= 0 and current_cell[0] < len(grid) \
				and current_cell[1] >= 0 and current_cell[1] < len(grid[0]):
					if original_grid[current_cell[0]][current_cell[1]] == "#":
						visible_occupied_seats += 1
						break
					if original_grid[current_cell[0]][current_cell[1]] == "L":
						break
					current_cell = (current_cell[0] + r, current_cell[1] + c)
			if original_grid[row][col] == "L" and visible_occupied_seats == 0:
				grid[row][col] = "#"
				changes_occurred = True
			elif original_grid[row][col] == "#" and visible_occupied_seats >= 5:
				grid[row][col] = "L"
				changes_occurred = True
	return changes_occurred

grid = read_grid_from_file()
while(update_state(grid)):
	pass
print(sum(str(r).count("#") for r in grid))

grid = read_grid_from_file()
while(update_state_v2(grid)):
	pass
print(sum(str(r).count("#") for r in grid))
