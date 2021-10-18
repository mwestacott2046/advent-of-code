
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

  def get_name (self):
    return self.name


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
    colon_pos = rule.find(':')
    name = rule[:colon_pos]
    rule_remain = rule[colon_pos+1:]
    or_spit = rule_remain.split('or')    
    lower1, upper1 = get_range(or_spit[0].strip())
    lower2, upper2 = get_range(or_spit[1].strip())
    validator = rule_validator(name, lower1, upper1, lower2, upper2)
    rules.append(validator)

  return rules

def str_to_int_list(line):
  string_vals = line.split(',')
  return list(map(int, string_vals))


def make_tickets (data):
  return list(map(str_to_int_list, data))


def is_value_valid_for_any(rules, value):
  for rule in rules:
    if rule.validate(value):
      return True
  
  return False

def is_ticket_valid(rules, ticket):
  for val in ticket:
    if not is_value_valid_for_any(rules, val):
      return False
  return True

def guess_columns(rules, tickets):
  ticket_len = len(tickets[0])
  rule_names = [rule.name for rule in rules]
  column_rules = {c: set(rule_names) for c in range(ticket_len)}

  for ticket in tickets:
    for col in range(ticket_len):
      for rule in rules:
        if not rule.validate(ticket[col]):
          column_rules[col].remove(rule.name)

  exclude_cols = set()
  solved_col, solved_rule= get_column_with_single_rule(column_rules, exclude_cols)

  while solved_col > -1:
    exclude_cols.add(solved_col)

    # remove rule
    for col, rule_set in column_rules.items():
      if col != solved_col:
        if solved_rule in rule_set:
          rule_set.remove(solved_rule)
          
    solved_col, solved_rule= get_column_with_single_rule(column_rules, exclude_cols)

  rule_map = { next(iter(v)): k for k, v in column_rules.items()}
  return rule_map
  

def get_column_with_single_rule(col_rule_dictionary, exclude_cols_ids):
  for col_id, rule_set in col_rule_dictionary.items():
    if col_id not in exclude_cols_ids:
      if len(rule_set) ==1:
        return col_id, next(iter(rule_set))
  
  return -1, ''


def remove_invalid_items(rules, other_tickets):
  valid_items = []
  for ticket in other_tickets:
      if is_ticket_valid(rules, ticket):
        valid_items.append(ticket)
  return valid_items


if __name__ == '__main__':

  rule_data, ticket_data, nearby_ticket_data = load_data('aoc-2020-16-input')
  rules = make_rules(rule_data)
  my_ticket = str_to_int_list(ticket_data[0])
  other_tickets = remove_invalid_items(rules, make_tickets(nearby_ticket_data))
  
  col_map = guess_columns(rules, other_tickets)
  departure_cols = [ v  for k, v in col_map.items() if k.startswith('departure')]

  result = 1
  for col in departure_cols:
    result *= my_ticket[col]
  
  print('result', result)
  