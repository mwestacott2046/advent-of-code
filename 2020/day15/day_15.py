
from collections import defaultdict


def play_game(start_numbers, end_turn):
  last_turns ={}

  for idx, val in enumerate(start_numbers[0:-1]):
    last_turns[val] = idx +1
    
  latest = start_numbers[-1]
  turn = len(start_numbers) + 1

  while turn <= end_turn:
    if latest not in last_turns.keys():
      last_turns[latest] = turn -1
      latest =0
    else:
      last_found = last_turns[latest]
      last_turns[latest] = turn -1
      latest = turn -1 - last_found
    turn +=1

  return latest

if __name__ == '__main__':

  # print (play_game([0,3,6], 2020))
  print ('part 1', play_game([2,15,0,9,1,20], 2020))
  print ('part 2', play_game([2,15,0,9,1,20], 30000000))

