def load_adapters (filename):
  values = []
  df = open(filename, 'r')
  file_data = df.readlines()
  df.close()

  for item in file_data:
    value = int(item.strip())
    values.append(value)

  return values


def build_adapter_list(adapters):
  sorted_list = sorted(adapters)
  diffs = {}
  previous = 0
  device_interval = 3
  for adapter in sorted_list:
    diff = adapter - previous
    if diff > 3:
      print('difference to big from {} to {} is {}'.format(previous, adapter, diff))
      return 0

    print('start: {} adapter: {} diff: {}'.format(previous, adapter, diff))
    
    diffs[diff] = diffs.get(diff,0) +1
    previous = adapter

  #include jump to device
  diffs[device_interval] = diffs.get(device_interval,0) +1

  print('diffs',diffs)
  return diffs.get(1,0) * diffs.get(3,0)


# adapters = load_adapters('test-data-1')
# adapters = load_adapters('test-data-2')
adapters = load_adapters('aoc-2020-10-input')

print(build_adapter_list(adapters))
