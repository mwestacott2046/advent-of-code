import re

def load_data (filename):
  with open(filename,'r') as df:
    data = df.readlines()
  
  lines = [line.strip() for line in data]
  empty_line = lines.index('')
  rule_data = lines[:empty_line]
  rule_dict = {}

  for rule in rule_data:
    id_split = rule.split(':')
    rule_id = int(id_split[0])
    rule_str =  id_split[1].strip()

    if rule_str.startswith('"'):
      rule_dict[rule_id] = rule_str.replace('"','')
    else:
      split_pipe = rule_str.split("|")
      rules=[]
      for r in split_pipe:
          rule_def = [ int(i) for i in r.split() ]
          rules.append(rule_def)

      rule_dict[rule_id] = rules

  messages = lines[empty_line+1:]
  return rule_dict, messages


def build_seq(rules,seq):
  if len(seq) ==0:
    return ""
  generated =[]
  for rule_id in seq:
    generated.append(generate_matches(rules, rule_id))

  return ''.join(generated)
  

def generate_matches (rules:dict, rule_id:int):

  rule = rules[rule_id]
  if isinstance(rule, list):
    results =[]
    for possibles in rule:
      results.append(build_seq(rules, possibles))

    if len(results) >1:
      return '({})'.format('|'.join(results))
    else:
      return results.pop()
  else:
    return rule


def get_matches(rules, messsages) -> int:
  matches = 0
  match_expr = generate_matches(rules, 0)
  for message in messsages:
    if re.fullmatch(match_expr,message) != None:
      matches +=1

  return matches


# rules, messsages = load_data('test-input')
rules, messsages = load_data('aoc-2020-19-input')

# print(generate_matches(rules,0))
print('matches:', get_matches(rules, messsages))


