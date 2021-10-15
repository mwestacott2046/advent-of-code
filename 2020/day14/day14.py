def load_lines(filename):
  data = []
  with open(filename, 'r') as df:
    lines = df.readlines()

  for line in lines:
    data.append(line.strip())

  return data

def int2bin(val:int):
  return format(val, '036b')


def bin2int(bin_string: str):
  return int(bin_string,2)


def get_mask(mask_line):
  tokens = mask_line.split('=')
  return tokens[1].strip()


def get_address_and_value(memory_line):
  tokens = memory_line.split('=')
  left = 1 + tokens[0].find('[')
  right = tokens[0].find(']')
  address = int(tokens[0][left:right])

  value = int(tokens[1].strip())
  # print('address', address, 'value', value)
  return address, value


def get_masked_value(mask, value):
  binary_value = int2bin(value)
  length = min(len(mask), len(binary_value))
  result = list('0' * length)

  for i in range (length-1,-1,-1):
    mask_val = mask[i]
    if mask_val == 'X':
      result[i] = binary_value[i]
    elif mask_val == '0':
      result[i] = '0'
    elif mask_val == '1':
      result[i] = '1'

  masked_val = bin2int(''.join(result))
  # print ('masked_val:', masked_val)
  return masked_val


def process_program(program):

  program_memory = {}

  mask = 'X' * 36
  for line in program:
    pass
    if line.startswith('mask'):
      mask = get_mask(line)
    elif line.startswith('mem'):
      address, value = get_address_and_value(line)
      program_memory[address] = get_masked_value(mask, value)

  return sum(program_memory.values())

program = load_lines('aoc-2020-14-input')
# program = load_lines('test-input')
print('result:', process_program(program))

