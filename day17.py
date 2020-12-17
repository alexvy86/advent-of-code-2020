from collections import defaultdict

initial_state = [
	"####.#..",
	".......#",
	"#..#####",
	".....##.",
	"##...###",
	"#..#.#.#",
	".##...#.",
	"#...##.."]

neighbors = [(z,x,y) for x in range(-1,2) for y in range(-1,2) for z in range(-1,2) if (z,x,y) != (0,0,0)]

def next_state(cell, cube):
	alive_neighbors = sum(1 for (z,x,y) in neighbors if cube[cell[0] + z][cell[1] + x][cell[2] + y] == "#")
	if cube[cell[0]][cell[1]][cell[2]] == "#":
		return "#" if alive_neighbors in [2,3] else "."
	else:
		return "#" if alive_neighbors in [3] else "."

infinite_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))
for x, row in enumerate(initial_state):
	for y, col in enumerate(row):
		infinite_cube[0][x][y] = col

z_min = z_max = x_min = y_min = 0
x_max = len(initial_state) - 1
y_max = len(initial_state[0]) - 1

for i in range(6):
	#print(f"Step {i}")
	new_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))
	for z in range(z_min - 1, z_max + 2):
		for y in range(y_min - 1, y_max + 2):
			for x in range(x_min - 1, x_max + 2):
				new_cube[z][x][y] = next_state((z, x, y), infinite_cube)
				if new_cube[z][x][y] == "#":
					z_min = min(z_min, z)
					z_max = max(z_max, z)
					x_min = min(x_min, x)
					x_max = max(x_max, x)
					y_min = min(y_min, y)
					y_max = max(y_max, y)
	infinite_cube = new_cube
	# for z in range(min_z, max_z + 1):
	# 	for x in range(min_x, max_x + 1):
	# 		print("".join(cell for cell in infinite_cube[z][x].values()))

print(sum(1 for x in range(x_min,x_max+1) for y in range(y_min,y_max+1) for z in range(z_min,z_max+1) if infinite_cube[z][x][y] == "#"))
