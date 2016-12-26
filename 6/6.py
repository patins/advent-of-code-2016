import sys

msgs = sys.stdin.read().strip().split('\n')

freqs = [dict() for _ in range(len(msgs[0]))] 

for msg in msgs:
    for i in range(len(msgs[0])):
        c = msg[i]
        freqs[i][c] = freqs[i].get(c, 0) + 1

answer = []
answer2 = []
for i in range(len(msgs[0])):
    answer.append(max(freqs[i], key=freqs[i].get))
    answer2.append(min(freqs[i], key=freqs[i].get))

print(''.join(answer))
print(''.join(answer2))
