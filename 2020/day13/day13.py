def load_timetable(filename):
  times_file = open(filename, 'r')
  depart_time = int(times_file.readline())
  bus_data = times_file.readline()

  split_times = bus_data.split(',')
  bus_intervals = list(map(int, filter (lambda i: i != 'x', split_times)))

  return depart_time, bus_intervals


def calc_next_departure (departure_time, bus):
  multiplier = departure_time // bus
  next_depart = bus * (multiplier +1)
  return next_depart


def find_departure_time (departure_time, intervals):
  bus_id = 0

  best_times = {}
  for bus in intervals:
    departs = calc_next_departure (departure_time, bus)
    wait_time = departs - departure_time
    best_times[wait_time]=bus

  min_wait = min(best_times.keys())
  bus_id = best_times[min_wait]
  return bus_id, min_wait


if __name__ == '__main__':
  # departure_time, intervals = load_timetable('test-input')
  departure_time, intervals = load_timetable('aoc-2020-13-input')
  bus_id, mins_to_wait = find_departure_time (departure_time, intervals)
  print('bus id', bus_id, 'mins to wait', mins_to_wait)
  print('result', bus_id * mins_to_wait)
