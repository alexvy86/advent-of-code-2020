from utils import read_lines

def is_valid(number, addends):
	for i in range(len(addends) - 1):
		for j in range (i + 1, len(addends)):
			if addends[i] + addends[j] == number:
				return True
	return False

numbers = [int(line) for line in read_lines(9)]

last_25 = []
invalid_number = -1
for number in numbers:
	if len(last_25) < 25:
		last_25.append(number)
	else:
		if is_valid(number, last_25):
			last_25.pop(0)
			last_25.append(number)
		else:
			invalid_number = number
			break

print(invalid_number)

lower_index = 0
upper_index = 1
current_sum = numbers[0] + numbers[1]

while current_sum != invalid_number:
	if current_sum < invalid_number:
		upper_index += 1
		current_sum += numbers[upper_index]
	else:
		current_sum -= numbers[lower_index]
		lower_index += 1

smallest = largest = numbers[lower_index]

for i in range(lower_index + 1, upper_index + 1):
	smallest = numbers[i] if numbers[i] < smallest else smallest
	largest = numbers[i] if numbers[i] > largest else largest

print(smallest + largest)