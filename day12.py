from utils import read_lines

current_pos = 0 + 0j
current_direction = 1 + 0j
rotations = {0: 1, 90: 1j, 180: -1, 270: -1j }

for instruction in read_lines(12):
	op, num = (instruction[0], int(instruction[1:]))
	#print(f"{current_pos} - {current_direction} - {op} {num}")
	if op == "N":
		current_pos += num * 1j
	if op == "S":
		current_pos -= num * 1j
	if op == "E":
		current_pos += num
	if op == "W":
		current_pos -= num
	if op == "F":
		current_pos += current_direction * num
	if op == "L":
		current_direction *= rotations[num % 360]
	if op == "R":
		current_direction *= rotations[(360 - num) % 360]

print(abs(current_pos.real) + abs(current_pos.imag))