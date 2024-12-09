safe_count = 0
for line in open('input.txt', 'r').readlines():
    vals = line.strip().split(' ')
    if len(vals) < 2:
        safe_count += 1
        continue

    i = int(vals[0])
    is_increasing = int(vals[1]) > i

    safe = True
    for va in vals[1:]:
        val = int(va)
        if (val > i) != is_increasing or abs(val - i) not in range(1,4):
            safe = False
            break
        i = val

    if safe:
        safe_count += 1

print(safe_count)