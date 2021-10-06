from math import ceil

def load_boarding_data():
  passes =[]
  df = open('aoc-2020-5-input', 'r')
  lines = df.readlines()
  for line in lines:
    passes.append(line.strip())

  return passes


def calculate_seat_id(boarding_card):
  row = calculate_row(boarding_card)
  column = calculate_column(boarding_card)

  seat_id = (row * 8) + column
  return seat_id


def calculate_column(boarding_card):
  col_min = 0
  col_max = 7

  for col_selector in boarding_card[7:]:
    if col_selector == 'L':
      col_max = (col_max + col_min) //2
    elif col_selector =='R':
      col_min = ceil((col_max + col_min) /2)
  
  return col_min


def calculate_row(boarding_card):
    row_min = 0
    row_max = 127

    for row_selector in boarding_card[:7]:
      if row_selector == 'F':
        row_max = (row_max + row_min) //2
      elif row_selector =='B':      
        row_min = ceil((row_max + row_min) /2)
        
    return row_min


def get_highest_seat_id(boarding_passes):
  max_id =0
  for boarding_pass in boarding_passes:
    seat_id = calculate_seat_id(boarding_pass)
    if seat_id > max_id:
      max_id = seat_id
  
  return max_id

def find_your_seat(boarding_passes):
  mapped_seats = set(map(calculate_seat_id, boarding_passes))
  min_seat = min(mapped_seats)
  max_seat = max(mapped_seats)

  for seat in range(min_seat, max_seat+1):
    if seat not in mapped_seats:
      return seat

  return -1

if __name__ == '__main__':
  print(find_your_seat(load_boarding_data()))