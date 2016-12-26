def input_to_end_coordinates(inp):
    inp = inp.strip().split(', ')
    pos = [0,0]
    d = 0
    # 0 - +y
    # 1 - +x
    # 2 - -y
    # 3 - -x
    visited = set([(0,0)])
    for i in inp:
        turn, steps = i[0], int(i[1:])
        if turn == 'L':
            d = (d-1) % 4
        if turn == 'R':
            d = (d+1) % 4
        if d == 0:
            pc, x = 1, 1
        elif d == 1:
            pc, x = 0, 1
        elif d == 2:
            pc, x = 1, -1
        elif d == 3:
            pc, x = 0, -1
        for _ in range(steps):
            pos[pc] += x
            if visited != None and tuple(pos) in visited:
                print(sum(map(abs, pos)))
                visited = None
            if visited != None:
                visited.add(tuple(pos))
    return tuple(pos)

end_coords = input_to_end_coordinates(input())
print(sum(map(abs, end_coords)))
