import sys

triangles = []

hist = []

for row in sys.stdin.read().strip().split('\n'):
    col = list(map(int, filter(None, row.strip().split(' '))))
    hist.append(col)

for ri in range(len(hist)//3):
    i = ri*3
    for c in range(3):
        triangles.append([hist[i][c], hist[i+1][c], hist[i+2][c]])

for sides in triangles:
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        print(sides)
