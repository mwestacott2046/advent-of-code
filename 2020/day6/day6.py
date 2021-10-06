def load_customs_data():
  data =[]
  df = open('aoc-2020-6-input', 'r')
  lines = df.readlines()
  for line in lines:
    data.append(line.strip())

  return data


def process_customs_data (customs_data):
  question_counts =[]
  group_data = set()
  for line in customs_data:
    if len(line) ==0:
      question_counts.append(len(group_data))
      group_data = set()
    else:
      for question in line:
        group_data.add(question)

  if len(question_counts) !=0:
    question_counts.append(len(group_data))
  
  return sum(question_counts)


print (process_customs_data (load_customs_data()))
