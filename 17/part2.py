# inspired by the solution of reddit.com/u/4HbQ

f = open('input.txt', 'r').readlines()
prog = list(map(int, f[4].strip().split(': ')[1].split(',')))

def run(a,b,c):
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
    return out

results = []
def find(a, tail_depth):
    res = run(a,0,0)
    if res == prog:
        results.append(a)

    elif res == prog[-tail_depth:] or tail_depth == 0:
        for n in range(8):
            find((a * 8) + n, tail_depth + 1)

find(0, 0)
print(min(results))
