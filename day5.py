from utils import read_lines

max_seat_id = 0
min_seat_id = 127 * 8 + 7
actual_seat_id_sum = 0

for line in read_lines(5):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

    for char in line:
        if char == "F":
            max_row = (max_row + min_row) // 2
        elif char == "B":
            min_row = (max_row + min_row) // 2 + 1
        elif char == "L":
            max_col = (max_col + min_col) // 2
        elif char == "R":
            min_col = (max_col + min_col) // 2 + 1
        #print(f"{char} {min_row} {max_row} {min_col} {max_col}")

    seat_id = min_row * 8 + min_col
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    if seat_id < min_seat_id:
        min_seat_id = seat_id

    actual_seat_id_sum += seat_id
print(max_seat_id)

sum_of_seat_ids_to_max = max_seat_id * (max_seat_id + 1) / 2 
sum_of_seat_ids_below_min = (min_seat_id - 1) * (min_seat_id) / 2

my_seat_id = sum_of_seat_ids_to_max - sum_of_seat_ids_below_min - actual_seat_id_sum
print(my_seat_id)
