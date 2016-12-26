import sys
import re
import string

prog = re.compile('([a-z\-]+)-(\d+)\[(\w+)\]')

def checksum(w):
    w = w.replace('-', '')
    dc = {}
    for c in w:
        dc[c] = dc.get(c, 0) + 1
    return ''.join(sorted(dc.keys(), key=lambda c: (-dc[c], c))[:5])

def shift(w, n):
    out = []
    for c in w:
        if c == '-':
            out.append(' ')
        else:
            i = string.ascii_lowercase.index(c)
            out.append(string.ascii_lowercase[(i+n) % 26])
    return ''.join(out)
n = 0
for line in sys.stdin.read().strip().split('\n'):
    name, sector, cs = prog.match(line).groups()
    sector = int(sector)
    if checksum(name) == cs:
        n += sector
        print(shift(name, sector), sector)
print(n)
