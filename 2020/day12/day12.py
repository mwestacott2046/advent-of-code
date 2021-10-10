
def load_instuctions(filename):
  instructions_file = open(filename,'r')
  lines = instructions_file.readlines();
  instructions_file.close()

  instructions = []
  for line in lines:
    instructions.append(line.strip())

  return instructions

def decode_instruction (instruction):
  return (instruction[:1], int(instruction[1:]))


def turn_left(current_direction, degrees):
  turn_left_lookup = {
    'E': 'N',
    'N': 'W',
    'W': 'S',
    'S': 'E',
    }
  
  while degrees > 0:
    current_direction = turn_left_lookup[current_direction]
    degrees -=90

  return current_direction


def turn_right(current_direction, degrees):
  turn_right_lookup = {
    'E': 'S',
    'S': 'W',
    'W': 'N',
    'N': 'E',
    }
  while degrees > 0:
    current_direction = turn_right_lookup[current_direction]
    degrees -=90

  return current_direction


def move_ship (command, distance, current_position):
  north_south, east_west = current_position
  
  if command == 'N':
    north_south += distance
  elif command == 'S':
    north_south += (distance * -1)
  elif command == 'E':
    east_west += distance
  elif command == 'W':
    east_west += (distance *-1)

  # print ('N/S', north_south, 'E/W', east_west)
  return (north_south, east_west)

def process_instructions (instructions):

  direction = 'E'
  position = (0,0) # +N/-S, +E/-W

  for instr in instructions:
    command, param = decode_instruction(instr)
    # print(command, param)
    if command =='F':
      position = move_ship (direction, param, position)
      pass
    elif command =='R':
      direction = turn_right(direction, param)
    elif command =='L':
      direction = turn_left(direction, param)
    else:
      position = move_ship (command, param, position)
      pass

  return position

def calc_manhattan_distance (position):
  ns, ew = position
  return abs(ns) + abs(ew)


instructions = load_instuctions('aoc-2020-12-input')
# instructions = load_instuctions('test-input')

position = process_instructions(instructions)
# print (position)
print('Manhattan Distance', calc_manhattan_distance (position))

