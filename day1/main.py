import itertools

ip = [int(l.rstrip()) for l in open('input.txt', 'r').readlines()]
print(ip)

two_combos = list(itertools.combinations(ip, 2))
pair = list(filter(lambda c: c[0] + c[1] == 2020, two_combos))
print(pair[0][0] * pair[0][1])

three_combos = list(itertools.combinations(ip, 3))
pair = list(filter(lambda c: c[0] + c[1] + c[2] == 2020, three_combos))
print(pair[0][0] * pair[0][1] * pair[0][2])

# for c in two_combos:
#   if c[0] + c[1] == 2020:
#     print(c[0] * c[1])

# two_combos = itertools.combinations(ip, 3)
# for c in two_combos:
#   if c[0] + c[1] == 2020:
#     print(c[0] * c[1])

# for i in range(0, len(ip)):
#   for j in range(i, len(ip)):
#     for z in range(j, len(ip)):
#       if ip[i] + ip[j] + ip[z] == 2020:
#         print(ip[i], ip[j], ip[z])
#         print(ip[i]*ip[j]*ip[z])
#         exit