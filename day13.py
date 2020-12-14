from utils import read_lines
import math
from functools import reduce

earliest_departure, bus_ids = read_lines(13)
earliest_departure = int(earliest_departure)
bus_ids = [(i[0], int(i[1])) for i in enumerate(bus_ids.split(",")) if i[1] != "x"]

min_data = (-1, math.inf)

for _, i in bus_ids:
	mins_to_wait = 0 if earliest_departure % i == 0 else i - (earliest_departure % i) 
	if mins_to_wait < min_data[1]:
		min_data = (i, mins_to_wait)

print(min_data[0] * min_data[1])

index_1 = bus_ids[0][0]
id_1 = bus_ids[0][1]
step = id_1
t = step
for index_2, id_2 in bus_ids[1:]:
	while (t + index_1) % id_1 != 0 or (t + index_2) % id_2 != 0:
		t += step
	step *= id_2

print(t)
