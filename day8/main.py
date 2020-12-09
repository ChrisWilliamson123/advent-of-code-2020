boot_code_input = [l.rstrip() for l in open('input.txt').readlines()]

def parse_instruction(i):
  split = i.split(' ')
  operation = split[0]
  value = split[1]
  return (operation, int(value))

def nop(x):
  global ip
  ip = ip + 1

def acc(v):
  global accumulator
  global ip
  accumulator += v
  ip += 1

def jmp(c):
  global ip
  ip += c

boot_code = list(map(parse_instruction, boot_code_input))

ip = 0
accumulator = 0

# List of indexes of instructions executed
executed = set()

next_i = boot_code[ip]

while ip not in executed:
  executed.add(ip)
  eval('{0}({1})'.format(next_i[0], next_i[1]))
  next_i = boot_code[ip]

print('Part 1: {0}'.format(accumulator))

nops = []
jmps = []

for i in range(0, len(boot_code)):
  instruction = boot_code[i][0]
  if instruction == 'nop':
    nops.append(i)
  elif instruction == 'jmp':
    jmps.append(i)

for n in nops:
  ip = 0
  accumulator = 0
  executed = set()
  next_i = boot_code[ip]
  while ip < len(boot_code) and ip not in executed:
    executed.add(ip)
    instruction = next_i[0]
    if ip == n:
      instruction = 'jmp'
    eval('{0}({1})'.format(instruction, next_i[1]))
    next_i = boot_code[ip]
  if ip == len(boot_code):
    print('part 2: {0}'.format(accumulator))

for j in jmps:
  ip = 0
  accumulator = 0
  executed = set()
  while ip < len(boot_code) and ip not in executed:
    next_i = boot_code[ip]
    executed.add(ip)
    instruction = next_i[0]
    if ip == j:
      instruction = 'nop'
    eval('{0}({1})'.format(instruction, next_i[1]))
  if ip == len(boot_code):
    print('part 2: {0}'.format(accumulator))
