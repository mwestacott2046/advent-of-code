targetValue =2020
def load_data():
  # load file values
  with open('aoc-2020-1-input','r') as df:
      lines = df.readlines()

# convert to int values
  values =[]
  for lineValue in lines:
    values.append(int(lineValue))
  return values


values = load_data()

def find_result(targetValue, values):
  values.sort()
  valueSet = set(values)
  found = False

  result = 0

  while not found and len(values) > 1:
    startValue = values.pop()
    searchValue = targetValue - startValue
    if searchValue in valueSet:
      found = True
      # print('StartValue', startValue, 'SearchValue', searchValue)
      result = searchValue * startValue

  return result


result = find_result(targetValue, values)
print('Result:', result)