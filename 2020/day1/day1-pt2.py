def load_data():
  # load file values
  with open('aoc-2020-1-input','r') as df:
      lines = df.readlines()

# convert to int values
  values =[]
  for lineValue in lines:
    values.append(int(lineValue))
  return values


def find_remaining_result(target, values):
  result = 0
  found = False
  remainingSet = set(values)

  while not found and len(values) > 1:
    startValue = values.pop()
    remaining = target - startValue

    if remaining in remainingSet:
      found = True
      result = startValue * remaining

  return result


def find_result(target, values):
  values.sort()
  found = False

  result = 0

  while not found and len(values) > 1:
    startValue = values.pop()
    remaining = target - startValue
    remainingValues = list(filter(lambda v: v < remaining, values))

    search_result = find_remaining_result(remaining, remainingValues)
    if search_result > 0:
      result = search_result * startValue
      found = True

  return result


targetValue =2020
values = load_data()
result = find_result(targetValue, values)
print('Result:', result)