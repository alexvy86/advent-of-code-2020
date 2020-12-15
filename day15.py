from utils import read_lines
from collections import defaultdict

starting_numbers = [int(n) for n in read_lines(15)[0].split(",")]

last_spoken_number = -1
spoken_numbers = defaultdict(lambda: (None, None))
for i, n in enumerate(starting_numbers):
	spoken_numbers[n] = (i, None)
	last_spoken_number = n

for i in range(len(starting_numbers), 30000000):
	new_number = 0 if spoken_numbers[last_spoken_number][1] == None \
								 else spoken_numbers[last_spoken_number][0] - spoken_numbers[last_spoken_number][1]
	spoken_numbers[new_number] = (i, spoken_numbers[new_number][0])
	last_spoken_number = new_number
	if i == 2019:
		print(last_spoken_number)

print(last_spoken_number)
