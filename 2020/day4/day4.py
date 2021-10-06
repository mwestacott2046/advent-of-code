import re

def make_passport(passport_string):
    passport = {}
    passport_items = passport_string.split()

    for item in passport_items:
        key_val_split = item.split(':')
        passport[key_val_split[0]] = key_val_split[1]

    return passport


def load_passport_data():
    passports = []
    df = open('aoc-2020-4-input', 'r')
    line = df.readline()

    current_passport_data = ''
    while line:
        line_data = line.strip()
        if len(line_data) > 0:
            current_passport_data += ' ' + line_data
        else:
            # process passport
            passports.append(make_passport(current_passport_data))
            current_passport_data = ''

        line = df.readline()

    if(len(current_passport_data)) > 0:
        passports.append(make_passport(current_passport_data))
    return passports


def validate_int_range(val, min_val, max_val):

    if val.isdecimal():
        val_int = int(val)
        if val_int >= min_val and val_int <= max_val:
            return True

    return False

def validate_year(year, min_year, max_year):
    if (len(year)) == 0:
        return False

    return validate_int_range(year, min_year, max_year)

def validate_height (height):
  if(len(height)) ==0:
    return False
  
  if height.endswith('in'):
    inch_digits = height.replace('in','')
    return validate_int_range(inch_digits, 59, 76)

  else:
    if height.endswith('cm'):
      cm_digits = height.replace('cm','')
      return validate_int_range(cm_digits, 150, 193)

  return False

def validate_hair_colour(hair):
  if(len(hair)) !=7:
    return False

  # r = re.compile(r'^#[0-9A-Fa-f]{3}', re.M)
  match = re.fullmatch('^#[0-9A-Fa-f]{6}',hair)
  if match != None:
    return True
  
  return False

def validate_eye_color(eyes):
  if(len(eyes)) ==0:
    return False

  valid_set = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
  if eyes in valid_set:
    return True
  
  return False

def validate_passport_id(pid):
  if(len(pid)) ==0:
    return False

  match = re.fullmatch('^[0-9]{9}',pid)
  if match != None:
    return True
  
  return False

def validate_passport(passport_dict):

    # byr (Birth Year)
    if not validate_year(passport_dict.get('byr', ''), 1920, 2002):
        # print('rejected - byr', passport_dict)
        return False

    # iyr (Issue Year)
    if not validate_year(passport_dict.get('iyr', ''), 2010, 2020):
        return False

    # eyr (Expiration Year)
    if not validate_year(passport_dict.get('eyr', ''), 2020, 2030):
        return False

    # hgt (Height)
    if not validate_height(passport_dict.get('hgt', '')):
        # print('rejected - hgt', passport_dict)
        return False

    # hcl (Hair Color)
    if not validate_hair_colour(passport_dict.get('hcl', '')):
        # print('rejected - hcl', passport_dict)
        return False

    # ecl (Eye Color)
    if not validate_eye_color(passport_dict.get('ecl', '')):
        # print('rejected - ecl', passport_dict)
        return False

    # pid (Passport ID)
    if not validate_passport_id(passport_dict.get('pid', '')):
        # print('rejected - pid', passport_dict)
        return False

    # cid (Country ID) Optional

    return True


def get_valid_count(passport_data):
    valid_count = 0
    for passport in passport_data:
        if validate_passport(passport):
            valid_count += 1

    return valid_count


# main program
passport_data = load_passport_data()
# print(passport_data)
print('passports:', len(passport_data))
print('valid passports:', get_valid_count(passport_data))
