def load_timetable(filename):
  times_file = open(filename, 'r')
  depart_time = int(times_file.readline())
  bus_data = times_file.readline()

  split_times = bus_data.split(',')

  return depart_time, split_times


# def sequntial_bus_times (start_time, bus_offsets):
#   for bus_id, offset in bus_offsets.items():
#     if (start_time + offset) % bus_id != 0:
#       return False

#   return True

def find_departure_time (intervals):
  bus_modulus = {}

  for time_offset, bus in enumerate(intervals):
    if bus != 'x':
      bus_int = int(bus)
      bus_modulus[bus_int] = (bus_int - time_offset) % bus_int

  # print(bus_modulus)

  vals = list(reversed(sorted(bus_modulus)))
  val = bus_modulus[vals[0]]
  print(vals)
  r = vals[0]
  for b in vals[1:]:
      while val % b != bus_modulus[b]:
          val += r
      r *= b
  return val

# Uses https://en.wikipedia.org/wiki/Chinese_remainder_theorem

if __name__ == '__main__':
  # departure_time, intervals = load_timetable('test-input')
  departure_time, intervals = load_timetable('aoc-2020-13-input')
  print(find_departure_time (intervals))
