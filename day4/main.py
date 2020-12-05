import re

passport_data = [l.rstrip() for l in open('input.txt', 'r').readlines()]

passports = []
current_passport = {}
for line in passport_data:
    if line == '':
        passports.append(current_passport)
        current_passport = {}
        continue
    entries = line.split(' ')
    for e in entries:
        kv = e.split(':')
        current_passport[kv[0]] = kv[1]
passports.append(current_passport)

full_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

validate_byr = lambda byr: 1920 <= int(byr) <= 2002
validate_iyr = lambda iyr: 2010 <= int(iyr) <= 2020
validate_eyr = lambda eyr: 2020 <= int(eyr) <= 2030
validate_ecl = lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
validate_hcl = lambda hcl: bool(re.compile('#[0-9a-f]{6}').match(hcl))
validate_pid = lambda pid: bool(re.compile('^[0-9]{9}$').match(pid))

def validate_hgt(hgt):
    units = hgt[-2:]
    if units != 'cm' and units != 'in':
        return False
    value = int(hgt[:-2])
    if units == 'cm':
        return 150 <= value <= 193
    else:
        return 59 <= value <= 76

def validate_passport(passport):
    if not set(full_keys).issubset(set(passport.keys())):
        return False
    for key in full_keys:
        valid = eval('validate_{0}(passport[\'{1}\'])'.format(key, key))
        if not valid:
            return False
    return True

valid_passports = filter(validate_passport, passports)
print(len(valid_passports))
