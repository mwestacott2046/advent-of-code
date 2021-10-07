
def load_bag_rules():
  data = []
  df = open('aoc-2020-7-input', 'r')
  # df = open('pt2-simple-test', 'r')
  lines = df.readlines()
  for line in lines:
    data.append(line.strip())

  return parse_bag_rules(data)

def parse_bag_rules (file_data):
  bag_rules = {}
  first_split_token= "bags contain"
  for line in file_data:
    bag_desc_end = line.find("bags contain")
    bag_desc = line[:bag_desc_end].strip()
    remaining = line[bag_desc_end + len(first_split_token) +1:]

    if remaining == "no other bags.":
      bag_rules[bag_desc] = {}
    else:
      container = {}
      remaining = remaining.replace(".","")
      remaining = remaining.replace("bags","")
      remaining = remaining.replace("bag","")

      items = remaining.split(",")
      for item in items:
        item = item.strip()
        name_start_pos = item.find(" ")
        qty = item[:name_start_pos].strip()
        contained_bag_name = item[name_start_pos +1:]
        container[contained_bag_name] = int(qty)

      bag_rules[bag_desc] = container

  return bag_rules


def calculate_bags_required(bag_rules, bag_name):

  current_rule = bag_rules[bag_name]
  if len(current_rule) == 0:
    return 1

  total_required = 1
  for sub_name, qty in current_rule.items():
    sub_required = calculate_bags_required(bag_rules, sub_name)
    total_required += (sub_required * qty)

  return total_required

bag_rules = load_bag_rules()
print ('total bags contained =',calculate_bags_required (bag_rules, "shiny gold") -1)

