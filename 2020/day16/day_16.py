
class rule_validator:

  def __init__(self, name:str, min1:int, max1:int, min2:int, max2:int):
    self.name = name
    self.min1 = min1
    self.max1 = max1
    self.min2 = min2
    self.max2 = max2

  def validate (self, val:int):
    if (val >= self.min1 and val <= self.max1) or (val >= self.min2 and val <= self.max2):
      return True

    return False


def load_data(filename):
  with open(filename, 'r') as df:
    data = df.readlines()
    
  file_data = list(map(lambda x: x.strip(),data))
  
  rules_end = file_data.index('')
  rules = file_data[:rules_end]

  my_ticket_end = file_data.index('',rules_end+1)
  my_ticket = file_data[rules_end+2: my_ticket_end]

  nearby_tickets = file_data[my_ticket_end+2:]
  
  return rules, my_ticket, nearby_tickets


def get_range(range_str:str):
  ranges = range_str.split('-')
  return int(ranges[0]), int(ranges[1])


def make_rules(rule_data):
  rules = []

  for rule in rule_data:
    # print('rule', rule)
    colon_pos = rule.find(':')
    name = rule[:colon_pos]
    rule_remain = rule[colon_pos+1:]
    or_spit = rule_remain.split('or')    
    lower1, upper1 = get_range(or_spit[0].strip())
    lower2, upper2 = get_range(or_spit[1].strip())
    # print('name', name, 'range', lower1, upper1, lower2, upper2)
    validator = rule_validator(name, lower1, upper1, lower2, upper2)
    rules.append(validator)

  return rules


def str_to_int_list(line):
  string_vals = line.split(',')
  return list(map(int, string_vals))


def make_tickets (data):
  return list(map(str_to_int_list, data))


def is_valid_for_any(rules, value):
  for rule in rules:
    if rule.validate(value):
      return True
  
  return False


def calc_error_rate(rules, other_tickets):
    ticket_errors = []
    for ticket in other_tickets:
      for val in ticket:
        if not is_valid_for_any(rules, val):
          ticket_errors.append(val)
    return sum(ticket_errors)



if __name__ == '__main__':

  rule_data, ticket_data, nearby_ticket_data = load_data('aoc-2020-16-input')
  # rule_data, ticket_data, nearby_ticket_data = load_data('test-input')
  rules = make_rules(rule_data)
  my_ticket = str_to_int_list(ticket_data[0])
  other_tickets = make_tickets(nearby_ticket_data)

  error_rate = calc_error_rate(rules, other_tickets)
  print('Error Rate:', error_rate)
