import itertools

data = [int(l.rstrip()) for l in open('input.txt').readlines()]

preamble = 25
lookback = 25

index = preamble

def number_is_valid(index, number):
  previous = data[index-lookback:index]
  pairs = list(itertools.combinations(previous, 2))
  for p in pairs:
    if sum(p) == number:
      return True
  return False

while index < len(data) and number_is_valid(index, data[index]):
  index += 1

print('Invalid number: {0}'.format(data[index]))

invalid = data[index]

for i in range(0, len(data)):
  current = data[i]
  for j in range(i+1, len(data)):
    current += data[j]
    if current == invalid:
      contiguous = data[i:j+1]
      print('Answer: {0}'.format(min(contiguous) + max(contiguous)))
    elif current > invalid:
      break