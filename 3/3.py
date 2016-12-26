import sys

for trs in sys.stdin.read().strip().split('\n'):
    sides = list(map(int, filter(None, trs.strip().split(' '))))
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        print(sides)
