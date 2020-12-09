from utils import read_lines

def is_valid(number, addends):
	for i in range(len(addends) - 1):
		for j in range (i + 1, len(addends)):
			if addends[i] + addends[j] == number:
				return True
	return False

last_25 = []
for number in (int(line) for line in read_lines(9)):
	if len(last_25) < 25:
		last_25.append(number)
	else:
		if is_valid(number, last_25):
			last_25.pop(0)
			last_25.append(number)
		else:
			print(number)
			break