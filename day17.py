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

def next_state(cell, cube):
	alive_neighbors = 0
	for offset in neighbor_offsets:
		neighbor = cube[tuple(cell[i] + offset[i] for i in range(dimensions))]
		if neighbor == "#":
			alive_neighbors += 1

	return "#" if (cube[cell] == "#" and alive_neighbors in [2,3]) or (cube[cell] == "." and alive_neighbors in [3]) else "."

infinite_cube = defaultdict(lambda: '.', {tuple([0]*(dimensions-2)) + (x,y): col for x, row in enumerate(initial_state) for y, col in enumerate(row)})

d_min_max[-2][1] = len(initial_state) - 1
d_min_max[-1][1] = len(initial_state[0]) - 1

for i in range(6):
	new_cube = defaultdict(lambda: '.')
	for coords in itertools.product(*(list(range(my_min - 1, my_max + 2)) for my_min, my_max in d_min_max)):
		new_cube[coords] = next_state(coords, infinite_cube)
		if new_cube[coords] == "#":
			for d, c in enumerate(coords):
				d_min_max[d][0] = min(d_min_max[d][0], c)
				d_min_max[d][1] = max(d_min_max[d][1], c)

	infinite_cube = new_cube

all_cube_coords = [c for c in itertools.product(*(list(range(my_min, my_max + 1)) for my_min, my_max in d_min_max))]
print(sum(1 for c in all_cube_coords if infinite_cube[c] == "#"))
