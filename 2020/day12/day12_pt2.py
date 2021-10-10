

def load_instuctions(filename):
  instructions_file = open(filename,'r')
  lines = instructions_file.readlines()
  instructions_file.close()

  instructions = []
  for line in lines:
    instructions.append(line.strip())

  return instructions

def decode_instruction (instruction):
  return instruction[:1], int(instruction[1:])


def rotate_left(degrees, waypoint):
  
  while degrees > 0:
    ns, ew = waypoint
    waypoint = (ew * 1, ns * -1)
    degrees -=90

  return waypoint


def rotate_right(degrees, waypoint):

  while degrees > 0:
    ns, ew = waypoint
    waypoint = (ew * -1, ns * 1)
    degrees -=90

  return waypoint


def move_waypoint (command, distance, waypoint_position):
  north_south, east_west = waypoint_position
  
  if command == 'N':
    north_south += distance
  elif command == 'S':
    north_south += (distance * -1)
  elif command == 'E':
    east_west += distance
  elif command == 'W':
    east_west += (distance *-1)

  return (north_south, east_west)

def move_ship(waypoint, multiplier, ship_position):
  wp_ns, wp_ew = waypoint
  sp_ns, sp_ew = ship_position

  sp_ns += (wp_ns * multiplier)
  sp_ew += (wp_ew * multiplier)

  return (sp_ns, sp_ew)


def process_instructions (instructions):

  position = (0,0) # +N/-S, +E/-W
  waypoint = (1, 10)

  for instr in instructions:
    command, param = decode_instruction(instr)
    if command =='F':
      position = move_ship (waypoint, param, position)
    elif command =='R':
      waypoint = rotate_right(param, waypoint)
    elif command =='L':
      waypoint = rotate_left(param, waypoint)
    else:
      waypoint = move_waypoint (command, param, waypoint)

  return position

def calc_manhattan_distance (position):
  ns, ew = position
  return abs(ns) + abs(ew)


instructions = load_instuctions('aoc-2020-12-input')
# instructions = load_instuctions('test-input')

position = process_instructions(instructions)
print('Manhattan Distance', calc_manhattan_distance (position))

