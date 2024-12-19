def is_possible(inpt):
    global towels
    reachable_counts = {0:1}
    reachable_idx = [0]
    for idx in reachable_idx:
        for towel in towels:
            if towel == inpt[idx:idx+len(towel)] and idx+len(towel) <= len(inpt):
                if idx + len(towel) not in reachable_idx:
                    reachable_idx.append(idx + len(towel))
                    reachable_idx.sort()
                reachable_counts[idx+len(towel)] = reachable_counts.get(idx+len(towel),0) + reachable_counts[idx]
    return reachable_counts.get(len(inpt),0)

f = open('input.txt', 'r').readlines()
towels = f[0].strip().split(', ')
f = f[2:]

res = 0
for line in f:
    res += is_possible(line.strip())
print(res)