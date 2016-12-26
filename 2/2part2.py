import sys

def coords_to_num(x, y):
    if y == 0:
        return 1
    if y == 1:
        return 2 + (x-1)
    if y == 2:
        return 5 + x
    if y == 3:
        return 'ABC'[x-1]
    if y == 4:
        return 'D'

def valid_coords(x, y):
    if y < 0 or y > 4:
        return False
    bound = 2 - abs(y-2)
    return x >= 2 - bound and x <= 2 + bound and y >= 0 and y <= 4

pos = [0, 2]
code = []
inp = sys.stdin.read()
for line in inp.strip().split('\n'):
    for instruction in line:
        dx, dy = 0, 0
        if instruction == 'L':
            dx = -1
        elif instruction == 'R':
            dx += 1
        elif instruction == 'U':
            dy -= 1
        else:
            dy += 1
        if valid_coords(pos[0] + dx, pos[1] + dy):
            pos[0] += dx
            pos[1] += dy
    code.append(coords_to_num(pos[0], pos[1]))

print(code)
