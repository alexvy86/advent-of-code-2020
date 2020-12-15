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
