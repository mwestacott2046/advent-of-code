# <bag desc> contain <n> <bag desc> [, <n> <bag desc> ] | "no other bags" .

def load_bag_rules():
  data = []
  df = open('aoc-2020-7-input', 'r')
  # df = open('test-input', 'r')
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
      bag_rules[bag_desc] = []
    else:
      container = []
      remaining = remaining.replace(".","")
      remaining = remaining.replace("bags","")
      remaining = remaining.replace("bag","")

      items = remaining.split(",")
      for item in items:
        item = item.strip()
        name_start_pos = item.find(" ")
        # qty = item[:name_start_pos].strip()
        contained_bag_name = item[name_start_pos +1:]
        container.append(contained_bag_name)

      bag_rules[bag_desc] = container

  return bag_rules


def can_contain_bag(bag_rules, current_rule_name, target_bag_name):

  current_rule = bag_rules[current_rule_name]
  if target_bag_name in current_rule:
      return True

  for bag_name in current_rule:
    if can_contain_bag(bag_rules, bag_name, target_bag_name):
      return True
  
  return False

bag_rules = load_bag_rules()
print(bag_rules)

bags_count =0
for rule_name in bag_rules.keys():
  if can_contain_bag(bag_rules, rule_name, "shiny gold"):
    bags_count +=1
    # print( rule_name)

print(bags_count)