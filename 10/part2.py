def discover_paths(working, f1):
    idx = 0
    while working:
        if idx == 9:
            return len(working)

        discover = []
        for el in working:
            if 0 < el[0]:
                discover.append([el[0]-1, el[1]])
            if 0 < el[1]:
                discover.append([el[0], el[1]-1])
            if len(f1) > el[0] + 1:
                discover.append([el[0]+1, el[1]])
            if len(f1[0].strip()) > el[1] + 1:
                discover.append([el[0], el[1]+1])
        working = []
        for el in discover:
            if int(f1[el[0]][el[1]]) == idx + 1:
                working.append(el)
        idx += 1
    return 0


f = open('input.txt', 'r').readlines()

zeros = []
for line_idx, line in enumerate(f):
    for char_idx, char in enumerate(line):
        if char == '0':
            zeros.append([[line_idx, char_idx]])

res = 0
for zero in zeros:
    res += discover_paths(zero, f)

print(res)