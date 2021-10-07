def load_program():
  data = []
  # df = open('aoc-2020-8-input', 'r')
  df = open('test-input', 'r')
  lines = df.readlines()
  for line in lines:
    data.append(line.strip())

  return parse_instuctions(data)


def parse_instuctions(program):
  operations = []
  for instuction in program:
    parts = instuction.split()
    operations.append((parts[0], int(parts[1])))

  return operations

def run_program(program):
  execution = []
  acc = 0
  pc = 0
  prev_pc = 0
  executed = set()
  while pc not in executed and pc < len(program):
    ic , arg = program[pc]
    executed.add(pc)
    if ic == 'nop':
      prev_pc = pc
      pc +=1
      execution.append("pc = {}, {}, {}, {}, jump-pos {}\n".format(prev_pc, ic, arg, acc, prev_pc + arg))
    elif ic == 'acc':
      acc += arg
      prev_pc = pc
      pc +=1
      execution.append("pc = {}, {}, {}, {}\n".format(prev_pc, ic, arg, acc))
    elif ic == 'jmp':
      prev_pc = pc
      pc += arg
      execution.append("pc = {}, {}, {}, {}, jump-to {}\n".format(prev_pc, ic, arg, acc, pc))

  if pc == len(program):
    execution.append('Execution Complete')
    print('Execution Complete')

  exec_log = open('exec.log', 'w')
  exec_log.writelines(execution)
  exec_log.close()

  return acc


program = load_program()
print('acc', run_program(program))
