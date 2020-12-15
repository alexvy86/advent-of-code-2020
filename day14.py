from utils import read_lines

mask_str = ""
mask_1_and = mask_2_or = 0
memory = {}
for line in read_lines(14):
	if line.startswith("mask"):
		mask_str = line[7:]
		mask_1_and = int(mask_str.replace("1", "0").replace("X", "1"), 2)
		mask_2_or = int(mask_str.replace("X", "0"), 2)
	else:
		part1, part2 = line.split("] = ")
		index = int(part1[4:])
		memory[index] = int(part2) & mask_1_and | mask_2_or

print(sum(v for v in memory.values()))

memory = {}
x_count = 0
for line in read_lines(14):
	if line.startswith("mask"):
		mask_str = line[7:]
		x_count = mask_str.count("X")
	else:
		part1, part2 = line.split("] = ")
		index = int(part1[4:])
		index_str = list(format(index, f"036b"))

		for i, c in enumerate(mask_str):
			if c == "1" or c == "X":
				index_str[i] = c

		for i in range(pow(2,x_count)):
			t = "".join(index_str)
			for c in format(i, f"0{x_count}b"):
				t = t.replace("X", c, 1)
			
			masked_index = int(t, 2)
			memory[masked_index] = int(part2)

print(sum(v for v in memory.values()))
