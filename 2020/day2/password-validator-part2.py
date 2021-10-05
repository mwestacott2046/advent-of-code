def split_password_data (password_line):
  split_colon = password_line.split(':')
  password = split_colon[1].strip()
  
  split_space = split_colon[0].split()
  validation_char = split_space[1]

  split_hyphen = split_space[0].split('-')
  min_chars = split_hyphen[0]
  max_chars = split_hyphen[1]

  return (password, validation_char, int(min_chars), int(max_chars))


def load_password_data():
  # load file values
  passwords = []
  with open('aoc-2020-2-input','r') as df:
    lines = df.readlines()

  for line in lines:
    if len(line) >0:
      passwords.append(split_password_data(line))
  
  return passwords


def validate (password, valid_char, min_chars, max_chars):

  char1 = password[min_chars-1]
  char2 = password[max_chars-1]

  if char1 == valid_char and char2 != valid_char:
    # print(char1, char2, valid_char, min_chars, max_chars, password, True)
    return True
  
  if char2 == valid_char and char1 != valid_char:
    # print(char1, char2, valid_char, min_chars, max_chars, password, True)
    return True

  # print(char1, char2, valid_char, min_chars, max_chars, password, False)

  return False


def validate_passwords (password_tuples):
  valid_count = 0

  for item in password_tuples:
    password, valid_char, min_chars, max_chars = item
    if validate (password, valid_char, min_chars, max_chars):
      valid_count += 1

  return valid_count



valid_count = validate_passwords(load_password_data())
print('Valid Passwords', valid_count)
