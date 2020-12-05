import math

passes = [l.rstrip() for l in open('input.txt', 'r').readlines()]

calc_new_lower_bound = lambda l, u: l + math.ceil((u - l) / 2)
calc_new_upper_bound = lambda l, u: u - math.ceil((u - l) / 2)

def binary_partition(spec, lower_char, upper_bound):
  lower_bound = 0
  for c in spec:
    if c == lower_char:
      upper_bound = calc_new_upper_bound(lower_bound, upper_bound)
    else:
      lower_bound = calc_new_lower_bound(lower_bound, upper_bound)
  return lower_bound

def calculate_seat_id(boarding_pass):
  row_spec = boarding_pass[0:7]
  row = binary_partition(row_spec, 'F', 127)

  column_spec = boarding_pass[-3:]
  col = binary_partition(column_spec, 'L', 7)

  return row * 8 + col

seat_ids = sorted(list(map(calculate_seat_id, passes)))

for i in range(1, len(seat_ids)):
  if seat_ids[i] - 1 != seat_ids[i-1]:
    print(seat_ids[i] - 1)
    exit

