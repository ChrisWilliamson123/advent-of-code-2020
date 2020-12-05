from functools import reduce

tree_map = [l.rstrip() for l in open('input.txt', 'r').readlines()]

max_y = len(tree_map) - 1
max_x = len(tree_map[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def take_slope(slope):
    x = y = crashes = 0
    while y < max_y:
        x += slope[0]
        y += slope[1]
        if tree_map[y][x % max_x] == '#':
            crashes += 1
    return crashes

answer = reduce(lambda x, y: x * y, map(take_slope, slopes))
print(answer)


