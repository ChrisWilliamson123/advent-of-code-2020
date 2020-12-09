import re

i = [l.rstrip() for l in open('input.txt', 'r').readlines()]

def build_graph(lines):
  graph = {}
  for l in i:
    regex = re.compile(r'^(\w+ \w+) bags contain (.+)\.$')
    match = regex.findall(l)[0]
    if match[-1] == 'no other bags':
      graph[match[0]] = []
      continue
    contains = match[-1].split(', ')
    values = list(map(lambda b: (re.compile(r'(\d+) (\w+ \w+) bags?').findall(b)[0][1], int(re.compile(r'(\d+) (\w+ \w+) bags?').findall(b)[0][0])), contains))
    graph[match[0]] = values
  return graph

graph = build_graph(i)

all_contains = set()
def contains(colour):
  return set(filter(lambda k: len([v[0] for v in graph[k] if v[0] == colour]) > 0, graph))

def check(colour):
  for c in contains(colour):
    check(c)
    all_contains.add(c)

check('shiny gold')

print(len(all_contains))

def count(colour, amount):
  current = 0
  children = graph[colour]
  if len(children) == 0:
    return amount
  for c in children:
    current += count(c[0], c[1])
  return (current * amount) + amount

print(count('shiny gold', 1) - 1)
    