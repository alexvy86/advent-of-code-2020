
from utils import read_lines

neighbor_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

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
	
grid = [list(f".{row}.") for row in read_lines(11)]
grid = [list("." * len(grid[0]))] + grid + [list("." * len(grid[0]))]

while(update_state(grid)):
	pass

print(sum(str(r).count("#") for r in grid))