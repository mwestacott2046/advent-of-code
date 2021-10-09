EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'


def load_seats(filename):
  seat_file = open(filename,'r')
  lines = seat_file.readlines();
  seat_file.close()

  seats = []
  for line in lines:
    seats.append(line.strip())

  return seats


def print_seating(seat_map):
    for line in seat_map:
      for col in line:
        print(col, end='')
      print()


def out_of_bounds(row_idx, col_idx, max_row_index, max_col_index):
  if row_idx < 0:
    return True
  if row_idx > max_row_index:
    return True
  if col_idx < 0:
    return True
  if col_idx > max_col_index:
    return True

  return False


def is_occupied_direction(row_increment, col_increment, seat_map, row_idx, col_idx, max_row_index, max_col_index):

  row_idx += row_increment
  col_idx += col_increment
  while not out_of_bounds(row_idx, col_idx, max_row_index, max_col_index):

    row = seat_map[row_idx]
    seat = row[col_idx]
    if seat == EMPTY_SEAT:
      return False
    elif seat == OCCUPIED_SEAT:
      return True

    row_idx += row_increment
    col_idx += col_increment

  return False


def get_populated_directional (seat_map, row_idx, col_idx, max_row_index, max_col_index):
  populated = 0

  #check left 0 -1
  if is_occupied_direction(0, -1, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1
  #check right 0 1
  if is_occupied_direction(0, 1, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1
  #check up -1 0
  if is_occupied_direction(-1, 0, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1
  #check down 1 0
  if is_occupied_direction(1, 0, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1

  #diagonal up left -1 -1
  if is_occupied_direction(-1, -1, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1
  #diagonal up right -1 1
  if is_occupied_direction(-1, 1, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1
  #diagonal down left 1 -1
  if is_occupied_direction(1, -1, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1
  #diagonal down right 1 1
  if is_occupied_direction(1, 1, seat_map, row_idx, col_idx, max_row_index, max_col_index):
    populated +=1

  return populated


def are_different(prev, next):
  for row_idx, prev_row in enumerate(prev):
    next_row = next[row_idx]
    for col_idx, prev_value in enumerate(prev_row):
      if prev_value != next_row[col_idx]:
        return True

  return False


def apply_seating_rules (seat_map):

  target_map = []
  max_row_index = len(seat_map) -1
  max_col_index = len(seat_map[0]) -1

  for row_idx, src_row in enumerate(seat_map):
    target_row =[]
    for col_idx, seat_value in enumerate(src_row):
      occupied = get_populated_directional(seat_map, row_idx, col_idx, max_row_index, max_col_index)
      if seat_value == EMPTY_SEAT and occupied == 0:
        seat_value = OCCUPIED_SEAT
      elif seat_value == OCCUPIED_SEAT and occupied >= 5:
        seat_value = EMPTY_SEAT

      target_row.append(seat_value)

    target_map.append(target_row)

  return target_map


def find_stable_map(seat_map):
  prev = seat_map
  next = apply_seating_rules(seat_map)
  while are_different(prev, next):
    prev = next
    next = apply_seating_rules(next)

  return next


def count_seated(seat_map):
  seated = 0
  for row in seat_map:
    for seat in row:
      if seat == OCCUPIED_SEAT:
        seated +=1

  return seated


# seat_map = load_seats('test-input')
seat_map = load_seats('aoc-2020-11-input')
result = find_stable_map(seat_map)

# print_seating(result)
print('seated:', count_seated(result))
