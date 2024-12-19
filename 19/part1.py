def is_possible(inpt):
    global towels
    reachable_idx = [0]
    for idx in reachable_idx:
        for towel in towels:
            if towel == inpt[idx:idx+len(towel)] and idx + len(towel) not in reachable_idx and idx+len(towel) <= len(inpt):
                if idx+len(towel) == len(inpt):
                    return 1
                else:
                    reachable_idx.append(idx + len(towel))
    return 0

f = open('input.txt', 'r').readlines()
towels = f[0].strip().split(', ')
f = f[2:]

res = 0
for line in f:
    res += is_possible(line.strip())
print(res)