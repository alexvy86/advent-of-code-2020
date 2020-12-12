from utils import read_lines

current_pos = current_pos_2 = 0 + 0j
current_direction = 1 + 0j
rotations = {0: 1, 90: 1j, 180: -1, 270: -1j }

waypoint_pos = 10 + 1j

for instruction in read_lines(12):
	op, num = (instruction[0], int(instruction[1:]))
	#print(f"{current_pos} - {current_direction} - {op} {num}")
	if op == "N":
		current_pos += num * 1j
		waypoint_pos += num * 1j
	elif op == "S":
		current_pos -= num * 1j
		waypoint_pos -= num * 1j
	elif op == "E":
		current_pos += num
		waypoint_pos += num
	elif op == "W":
		current_pos -= num
		waypoint_pos -= num
	else:
		waypoint_vector = (waypoint_pos - current_pos_2)
		if op == "F":
			current_pos += current_direction * num
			current_pos_2 += num * waypoint_vector
		elif op == "L":
			current_direction *= rotations[num % 360]
			waypoint_vector *= rotations[num % 360]
		elif op == "R":
			current_direction *= rotations[(360 - num) % 360]
			waypoint_vector *= rotations[(360-num) % 360]
		waypoint_pos = current_pos_2 + waypoint_vector

print(abs(current_pos.real) + abs(current_pos.imag))
print(abs(current_pos_2.real) + abs(current_pos_2.imag))