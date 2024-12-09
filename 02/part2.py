def is_safe(vals):
    if len(vals) < 2:
        return True
    i = int(vals[0])
    is_increasing = int(vals[1]) > i
    safe = True
    for va in vals[1:]:
        val = int(va)
        if (val > i) != is_increasing or abs(val - i) not in range(1,4):
            safe = False
            break
        i = val
    return safe

safe_count = 0
for line in open('input.txt', 'r').readlines():
    vals = line.strip().split(' ')

    alts = [vals]
    for j in range(len(vals)):
        alts.append(vals[:j] + vals[j+1:])

    for alt in alts:
        if is_safe(alt):
            safe_count += 1
            break

print(safe_count)