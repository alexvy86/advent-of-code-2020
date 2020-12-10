from utils import read_lines
from collections import defaultdict

jolt_ratings = [int(x) for x in read_lines(10)]
jolt_ratings.sort()

current_rating = 0
rating_diff_count = defaultdict(int)

for entry in jolt_ratings:
	diff = entry - current_rating
	rating_diff_count[diff] += 1
	current_rating = entry

# Consider the built-in joltage adapter 
rating_diff_count[3] += 1

print(rating_diff_count[1] * rating_diff_count[3])

memoized = {}
def count_arrangements(rating_list, start_pos):
	if start_pos in memoized:
		return memoized[start_pos]

	result = 1 if len(rating_list[start_pos:]) == 1 \
	           else sum(count_arrangements(rating_list, start_pos + i)
						  	      for i in range(1,4)
		                  if start_pos + i < len(rating_list) and rating_list[start_pos + i] <= rating_list[start_pos] + 3)
	memoized[start_pos] = result
	return result

# Add a 0 at the beginning to account for the different adapters that we can connect
# directly to the outlet
print(count_arrangements([0] + jolt_ratings, 0))