from collections import defaultdict
import itertools

initial_state = [	"####.#..",
									".......#",
									"#..#####",
									".....##.",
									"##...###",
									"#..#.#.#",
									".##...#.",
									"#...##.."]

dimensions = 4
d_min_max = [[0,0] for _ in range(dimensions)]
neighbor_offsets = list(list(x) for x in itertools.product([-1,0,1], repeat=dimensions) if x != tuple([0]*dimensions))

def nested_dictionary(d):
	if d == 1:
		return defaultdict(lambda: '.')
	else:
		return defaultdict(lambda: nested_dictionary(d - 1))

def next_state(cell_coords, cube):
	alive_neighbors = 0
	for offset in neighbor_offsets:
		neighbor = cube
		for dim in tuple(cell_coords[i] + offset[i] for i in range(dimensions)):
			neighbor = neighbor[dim]
		if neighbor == "#":
			alive_neighbors += 1

	cell = cube
	for dim in cell_coords:
			cell = cell[dim]
	return "#" if (cell == "#" and alive_neighbors in [2,3]) or (cell == "." and alive_neighbors in [3]) else "."

infinite_cube = nested_dictionary(dimensions)
for x, row in enumerate(initial_state):
	for y, col in enumerate(row):
		cell = infinite_cube
		for _ in range(dimensions-2):
			cell = cell[0]
		cell[x][y] = col

d_min_max[-2][1] = len(initial_state) - 1
d_min_max[-1][1] = len(initial_state[0]) - 1

for i in range(6):
	new_cube = nested_dictionary(dimensions)
	for coords in itertools.product(*(list(range(my_min - 1, my_max + 2)) for my_min, my_max in d_min_max)):
		new_cell = new_cube
		for dim in coords[:-1]:
			new_cell = new_cell[dim]
		new_value = next_state(coords, infinite_cube)
		new_cell[coords[-1]] = new_value
		if new_value == "#":
			for d, c in enumerate(coords):
				d_min_max[d][0] = min(d_min_max[d][0], c)
				d_min_max[d][1] = max(d_min_max[d][1], c)

	infinite_cube = new_cube

active_cubes = 0
all_cube_coords = [c for c in itertools.product(*(list(range(my_min, my_max + 1)) for my_min, my_max in d_min_max))]
for c in all_cube_coords:
	cell = infinite_cube
	for dim in c:
			cell = cell[dim]
	if cell == "#":
		active_cubes += 1
print(active_cubes)
