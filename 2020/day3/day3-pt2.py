def load_tree_data():
  route  = []  
  with open('aoc-day-3-input','r') as df:
    lines = df.readlines()

  for line in lines:
    route.append(line.strip())

  return route

def get_position (position, route_width):
  new_position = position % route_width
  return new_position -1

def calculate_route(route, right, down):
  route_width = len(route[0])
  tree_hits = 0
  position_across = 1

  for row in range(0,len(route), down):
    current_row = route[row]

    if current_row[get_position(position_across, route_width)] == '#':
      tree_hits +=1

    position_across += right


  return tree_hits

trees =1
trees *= calculate_route (load_tree_data(), 1, 1)
trees *= calculate_route (load_tree_data(), 3, 1)
trees *= calculate_route (load_tree_data(), 5, 1)
trees *= calculate_route (load_tree_data(), 7, 1)
trees *= calculate_route (load_tree_data(), 1, 2)

print('Trees', trees)
