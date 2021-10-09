def load_adapters (filename):
  values = []
  df = open(filename, 'r')
  file_data = df.readlines()
  df.close()

  for item in file_data:
    value = int(item.strip())
    values.append(value)

  return values


def make_key(start_val, values):
  key = str(start_val) + str(values)
  return key


def calc_permutations(start_val, lookups, max_value, perf_dict = {}):
  
  if start_val == max_value:
    return 1
  
  permutations = 0 
  values = lookups[start_val]
  
  key = make_key(start_val, values)
  if key in perf_dict:
    return perf_dict[key]
  
  for item in values:
    child_permutations = calc_permutations(item, lookups, max_value, perf_dict)
    permutations += child_permutations

  perf_dict[key] = permutations
  return permutations



def build_adapter_permutations(adapters):
  sorted_list = sorted(adapters)
  sorted_list.insert(0,0)
  max_item = max(sorted_list) +3
  sorted_list.append(max_item)
  lookups = {}
  for item in sorted_list:
    lookups[item] = list(filter(lambda x: x > item and x <= item+3, sorted_list))

  result = calc_permutations(0, lookups, max_item)
  return  result


# adapters = load_adapters('test-data-1')
# adapters = load_adapters('test-data-2')
adapters = load_adapters('aoc-2020-10-input')

permutations = build_adapter_permutations(adapters)
print('perm count', permutations)
