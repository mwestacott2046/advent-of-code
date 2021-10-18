from collections import defaultdict


ACTIVE = '#'
INACTIVE = '.'

def load_data(filename):
  with open(filename,'r') as df:
    data = df.readlines()

  return [line.strip() for line in data]

def make_key(row_pos, col_pos, z_pos):
  return '{}:{}:{}'.format(str(row_pos), str(col_pos), str(z_pos))


def populate_from_initial_state(initial_state, rows, cols):

    state = defaultdict(lambda : INACTIVE)
    row_pos = -(rows // 2)
    inital_row_pos = row_pos
    col_pos = -(cols // 2)
    z_pos = 0

    for row in initial_state:
      for item in row:
        state[make_key(row_pos, col_pos, z_pos)] = item
        col_pos +=1
      row_pos +=1
      col_pos = inital_row_pos
    return state


def get_active_cells(state, row_pos ,col_pos , z_pos):
  
  cell_values  = []
  #process z plane, excluding the center item
  cell_values.append(state[make_key(row_pos, col_pos-1, z_pos)])
  cell_values.append(state[make_key(row_pos, col_pos+1, z_pos)])
  for col in range(col_pos-1, col_pos+2):
    cell_values.append(state[make_key(row_pos-1, col, z_pos)])
    cell_values.append(state[make_key(row_pos+1, col, z_pos)])

  # now get values from z +/- 1
  for col in range(col_pos-1, col_pos+2):
    for row in range(row_pos -1, row_pos +2):
      cell_values.append(state[make_key(row, col, z_pos-1)])
      cell_values.append(state[make_key(row, col, z_pos+1)])

  return len(list(filter(lambda v: v == ACTIVE, cell_values)))
  


def simulate_step (state, row_upper, row_lower, col_upper, col_lower, z_upper, z_lower):
  next_state = defaultdict(lambda : INACTIVE)

  for row in range(row_lower, row_upper+1):
    for col in range(col_lower, col_upper+1):
      for z in range(z_lower, z_upper+1):
        active_cells = get_active_cells(state, row, col, z)
        position_key = make_key(row,col,z)
        cell = state[position_key]
        if cell == ACTIVE:
          if active_cells >=2 and active_cells <= 3:
            next_state[position_key] = ACTIVE
          else:
            next_state[position_key] = INACTIVE
        elif cell == INACTIVE:
          if active_cells ==3:
            next_state[position_key] = ACTIVE
          else:
            next_state[position_key] = INACTIVE
  
  return next_state


def simulate(initial_state, iterations):

  rows = len(initial_state)
  cols = len(initial_state[0])

  state = populate_from_initial_state(initial_state, rows, cols)

  row_upper = (rows + (iterations *2)) // 2
  row_lower = -row_upper
  col_upper = (cols + (iterations *2)) // 2
  col_lower = -col_upper
  z_upper, z_lower = col_upper, col_lower

  for _ in range (iterations):
    state = simulate_step (state, row_upper, row_lower, col_upper, col_lower, z_upper, z_lower)

  total_active = len(list(filter(lambda v: v == ACTIVE, state.values())))
  return total_active


initial_state = load_data('aoc-2020-17-input')
print('result', simulate(initial_state, 6))
