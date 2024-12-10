f = open('input.txt', 'r').readlines()
res = 0
for line in f:
    line = line.strip().split(':')
    result = int(line[0])
    vals = line[1].strip().split(' ')
    vals = list(map(int, vals))

    steps = {0: [vals[0]]}
    for i in range(1,len(vals)):
        for step in steps[i-1]:
            steps[i] = steps.get(i, []) + [step + vals[i], step * vals[i]]
    if result in steps[len(steps)-1]:
        res += result

print(res)