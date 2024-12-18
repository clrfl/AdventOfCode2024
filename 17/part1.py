f = open('input.txt', 'r').readlines()
a = int(f[0].strip().split(': ')[1])
b = int(f[1].strip().split(': ')[1])
c = int(f[2].strip().split(': ')[1])

prog = list(map(int, f[4].strip().split(': ')[1].split(',')))

out = []
pc = 0
while pc + 1 < len(prog):
    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}
    instr = prog[pc]
    op = prog[pc + 1]

    match instr:
        case 0: a = int(a >> combo[op])
        case 1: b = b ^ op
        case 2: b = combo[op] % 8
        case 3: pc = op - 2 if a else pc
        case 4: b = b ^ c
        case 5: out.append(combo[op] % 8)
        case 6: b = int(a >> combo[op])
        case 7: c = int(a >> combo[op])
    pc += 2

print(*out, sep=',')


