import re

ip = [l.rstrip() for l in open('input.txt', 'r').readlines()]
regex = re.compile('(\d+)-(\d+) (\w): (\w+)')
parsed = map(lambda l: regex.findall(l)[0], ip)

def check_password(entry):
    min_occurences, max_occurences, letter, password = entry
    occurences = password.count(letter)
    return int(min_occurences) <= occurences <= int(max_occurences)

def check_password_2(entry):
    letter = entry[2]
    password = entry[3]
    indexes = (int(entry[0])-1, int(entry[1])-1)
    return len(filter(lambda i: password[i] == letter, indexes)) == 1

print(len(filter(check_password, parsed)))
print(len(filter(check_password_2, parsed)))
