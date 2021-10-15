def load_lines(filename):
  data = []
  with open(filename, 'r') as df:
    lines = df.readlines()

  for line in lines:
    data.append(line.strip())

  return data


def int2bin(val:int, length=36):
  format_string = '0' + str(length) + 'b'
  return format(val, format_string)


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
  return masked_val

def generate_floating_values (float_mask: list, float_locations):
  values = []
  
  float_count = len(float_locations)
  bin_max = pow(2, float_count)

  for n in range(0, bin_max):
    mask_copy = float_mask.copy()
    binsrc = int2bin(n, float_count)
    for idx, pos in enumerate(float_locations):
      mask_copy[pos] = binsrc[idx]
    
    bin_val = ''.join(mask_copy)
    values.append(bin2int(bin_val))

  return values


def get_floating_values(mask, value):
  float_locations=[]
  binary_value = int2bin(value)
  length = min(len(mask), len(binary_value))
  float_mask = list('0' * length)

  for i in range (length-1,-1,-1):
    mask_val = mask[i]
    if mask_val == 'X':
      float_mask[i] = 'f'
      float_locations.append(i)
    elif mask_val == '0':
      float_mask[i] = binary_value[i]
    elif mask_val == '1':
      float_mask[i] = '1'

  floating_values = generate_floating_values (float_mask, float_locations)
  return floating_values


def process_program(program):
  bits = 36
  program_memory = {}

  mask = 'X' * bits
  for line in program:
    if line.startswith('mask'):
      mask = get_mask(line)
    elif line.startswith('mem'):
      address, value = get_address_and_value(line)
      floating_addresses = get_floating_values(mask, address)
      for addr in floating_addresses:
        program_memory[addr] = value

  return sum(program_memory.values())

program = load_lines('aoc-2020-14-input')
print('result:', process_program(program))

