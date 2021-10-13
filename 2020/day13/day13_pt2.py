def load_timetable(filename):
  times_file = open(filename, 'r')
  depart_time = int(times_file.readline())
  bus_data = times_file.readline()

  split_times = bus_data.split(',')

  return depart_time, split_times


def sequntial_bus_times (start_time, bus_offsets):
  for bus_id, offset in bus_offsets.items():
    if (start_time + offset) % bus_id != 0:
      return False

  return True

def find_departure_time (intervals):
  bus_offsets = {}

  for time_offset, bus in enumerate(intervals):
    if bus != 'x':
      bus_int = int(bus)
      bus_offsets[bus_int]= time_offset

  print(bus_offsets)

  first_interval = int(intervals[0])
  # print('first_interval', first_interval)
  start_time = first_interval

  while not sequntial_bus_times (start_time, bus_offsets):
    start_time += first_interval
    # if start_time % 100000000 == 0:
    #   print (start_time)

  return start_time

# This works for the smaller input, 
# but takes forever with the large input, 
# need to find a better way to do this!

if __name__ == '__main__':
  # departure_time, intervals = load_timetable('test-input')
  departure_time, intervals = load_timetable('aoc-2020-13-input')
  print(find_departure_time (intervals))
