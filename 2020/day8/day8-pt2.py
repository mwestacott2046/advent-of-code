def load_program():
  data = []
  df = open('aoc-2020-8-input', 'r')
  # df = open('test-input', 'r')
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

def run_program(program, write_log=True):
  execution = []
  acc = 0
  pc = 0
  prev_pc = 0
  executed = set()
  program_completed = False

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
    program_completed = True
    execution.append('Execution Complete')
    # print('Execution Complete')

  if write_log:
    exec_log = open('exec.log', 'w')
    exec_log.writelines(execution)
    exec_log.close()

  # print('acc', acc, 'pc',pc, 'prev', prev_pc, program[prev_pc])  
  return (acc, program_completed)


def permute_program_to_complete(program):
  permute_log = open('permutations.log', 'w')

  for modify_index in range(0, len(program)):
    op, arg = program[modify_index]
    if op == 'nop':
      permutation = program.copy()
      permutation[modify_index] = ('jmp',arg)
      acc, is_complete = run_program(permutation,False)
      permute_log.write("change index: {}, op: {}, acc: {}, is complete: {} \n".format(modify_index, op, acc, is_complete))
      if is_complete:
        return (True, acc, modify_index)
    elif op == 'jmp':
      permutation = program.copy()
      permutation[modify_index] = ('nop',arg)
      acc, is_complete = run_program(permutation, False)
      permute_log.write("change index: {}, op: {}, acc: {}, is complete: {} \n".format(modify_index, op, acc, is_complete))
      if is_complete:
        return (True, acc, modify_index)

  permute_log.close()
  return (False,0,0)


program = load_program()

print('completed, acc, modified', permute_program_to_complete(program))