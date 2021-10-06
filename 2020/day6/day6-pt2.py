def load_customs_data():
  data =[]
  df = open('aoc-2020-6-input', 'r')
  # df = open('test2', 'r')
  lines = df.readlines()
  for line in lines:
    data.append(line.strip())

  return data


def process_customs_data (customs_data):
  groups = []
  group_questions = {}
  group_passengers =0

  for line in customs_data:
    if len(line) ==0:
      groups.append((group_questions, group_passengers))
      group_questions = {}
      group_passengers =0
    else:
      group_passengers +=1
      for question in line:
        group_questions[question] = group_questions.get(question, 0) +1

  if len(group_questions) !=0:
    groups.append((group_questions, group_passengers))
  
  # count questions
  counts = []
  for group in groups:
    count = 0
    question_dict, passenger_count = group
    for v in question_dict.values():
      if v == passenger_count:
        count += 1

    counts.append(count)

  return sum(counts)


print (process_customs_data (load_customs_data()))
