import hashlib

door_id = input()
p = []

for n in range(int(10e10)):
    m = hashlib.md5()
    m.update(str(door_id + str(n)).encode('utf-8'))
    d = m.hexdigest()
    if d.startswith('00000'):
        p.append(d[5])
        print(d[5])
    if len(p) == 8:
        break

print(''.join(p))
