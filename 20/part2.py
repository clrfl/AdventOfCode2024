f = open('input.txt', 'r').readlines()
grid = []
start = []
end = []

for y, line in enumerate(f):
    for x, char in enumerate(line.strip()):
        if char == '.':
            grid.append([x, y])
        elif char == 'S':
            start = [x, y]
            grid.append(start)
        elif char == 'E':
            end = [x, y]
            grid.append(end)

# steps to finish from location:
stf = {str(end): 0}
queue = [end]

for el in queue:
    for x in [[el[0] - 1, el[1]], [el[0] + 1, el[1]], [el[0], el[1] - 1], [el[0], el[1] + 1]]:
        if x not in queue and x in grid:
            queue.append(x)
            stf[str(x)] = stf[str(el)] + 1

cheat_mask = []
for x in range(-20,21):
    for y in range(-20,21):
        if abs(x) + abs(y) <= 20:
            cheat_mask.append([[x, y], abs(x) + abs(y)])

res = 0
for el in queue:
    for val in cheat_mask:
        x = [el[0]+val[0][0], el[1]+val[0][1]]
        if stf[str(el)] - stf.get(str(x), 9E5) - val[1] >= 100:
            res += 1

print(res)
