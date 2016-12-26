import sys

def coords_to_num(x, y):
    return (3*y) + x + 1

def valid_coords(x, y):
    return x >= 0 and y >= 0 and x < 3 and y < 3

pos = [0, 0]
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
