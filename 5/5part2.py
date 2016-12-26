import hashlib

door_id = input()
p = [None] * 8
rem = 8
for n in range(int(10e10)):
    m = hashlib.md5()
    m.update(str(door_id + str(n)).encode('utf-8'))
    d = m.hexdigest()
    if d.startswith('00000'):
        if d[5].isdigit():
            pos = int(d[5])
            if pos < 8:
                if p[pos] == None:
                    p[pos] = d[6]
                    print(d[5], d[6])
                    rem -= 1
                    if rem == 0:
                        break

print(''.join(p))
