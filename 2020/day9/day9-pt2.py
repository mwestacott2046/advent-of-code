def load_numbers ():
  values = []
  df = open('aoc-2020-9-input', 'r')
  # df = open('test-input', 'r')
  file_data = df.readlines()

  for item in file_data:
    value = int(item.strip())
    values.append(value)

  return values

def composed_of(check_value, value_range):
  for num in value_range:
    to_find = check_value - num
    if to_find in value_range:
      return True
  
  return False

def find_invalid_xmas(data, preamble):
  pass
  item_index = preamble

  while item_index < len(data):
    range_start = item_index - preamble
    value_range = data[range_start: item_index]
    check_value = data[item_index]
    if not composed_of(check_value, value_range):
      return check_value
    
    item_index +=1

  return -1

def find_invalid_sum_range(data, target_num):
  range_result = []
  for range_start in range(0, len(data)-1):
    range_result = []
    range_result.append(data[range_start])
    next_item = range_start +1
    while sum(range_result) < target_num:
      range_result.append(data[next_item])
      next_item +=1

    if sum(range_result) == target_num:
      return range_result
  return []


def get_weakness(sum_range):
  return min(sum_range) + max(sum_range)


data = load_numbers()

preamble = 25
invalid_num = find_invalid_xmas(data, preamble)
sum_range = find_invalid_sum_range(data, invalid_num)
print (get_weakness(sum_range))
