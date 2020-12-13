from utils import read_lines
import math
from functools import reduce

earliest_departure, bus_ids = read_lines(13)
earliest_departure = int(earliest_departure)
bus_ids = [int(i) for i in bus_ids.split(",") if i != "x"]

min_data = (-1, math.inf)

for i in bus_ids:
	mins_to_wait = 0 if earliest_departure % i == 0 else i - (earliest_departure % i) 
	if mins_to_wait < min_data[1]:
		min_data = (i, mins_to_wait)

print(min_data[0] * min_data[1])