from functools import reduce

all_answers = open('input.txt', 'r').read()
print(all_answers)
groups = all_answers.split('\n\n')

# print(groups)

# current_group_yesses = []
# groups = []
# for l in all_answers:
#   if l == '':
#     groups.append(current_group_yesses)
#     current_group_yesses = []
#     continue
#   current_group_yesses.append(l)

# groups.append(current_group_yesses)

counts = []
for g in groups:
  all_exist = set()
  for c in g[0]:
    all_exist.add(c)
  for i in range(1, len(g)):
    all_exist = all_exist.intersection(set(g[i]))
  counts.append(len(all_exist))

print(sum(counts))
