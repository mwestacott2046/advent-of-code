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

data = load_numbers()
preamble = 25
print(find_invalid_xmas(data, preamble))
