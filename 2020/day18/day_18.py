from typing import List

def load_expressions (filename) -> List:
  with open(filename,'r') as df:
    data = df.readlines()

  return [line.strip() for line in data]


def calc_expression (expr:str) -> int:
  posfix_expr = infix_to_postfix(expr)

  return evaluate_postfix(posfix_expr)


def evaluate_postfix(postfix_expr):
  calc_stack = []
  for item in postfix_expr:
    if item.isdigit():
      calc_stack.append(int(item))
    elif item == '+':
      value2 = calc_stack.pop()
      value1 = calc_stack.pop()
      calc_stack.append(value1 + value2)
    elif item == '*':
      value2 = calc_stack.pop()
      value1 = calc_stack.pop()
      calc_stack.append(value1 * value2)

  result = calc_stack.pop()
  return result

def infix_to_postfix(expr):
    expression = []
    op_stack = []
    for ch in expr:
      if ch.isdigit():
        expression.append(ch)

      elif ch =='+' or ch =='*':
        while len(op_stack) > 0 and op_stack[-1] != '(':
          expression.append(op_stack.pop())
        op_stack.append(ch)

      elif ch == '(':
        op_stack.append(ch)

      elif ch == ')':
        # print('opstack', op_stack)
        while len(op_stack) != 0 and op_stack[-1] != '(':
          expression.append(op_stack.pop())
        op_stack.pop()

    while len(op_stack) != 0:
      expression.append(op_stack.pop())

    return expression

def get_sum_of_expressions(expressions: list) -> int:
  expr_sum = sum(map (calc_expression,expressions))
  return expr_sum


if __name__ == '__main__':

  expressions = load_expressions('aoc-2020-18-input')
  print(get_sum_of_expressions(expressions))