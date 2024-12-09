seen_old = []
facings = '^>v<'
def move(x, y, facing):
    if [x,y] not in seen_old:
        seen_old.append([x, y])

    if facing == '^':
        newx = x
        newy = y-1
    elif facing == 'v':
        newx = x
        newy = y+1
    elif facing == '>':
        newx = x+1
        newy = y
    elif facing == '<':
        newx = x-1
        newy = y

    if 0 <= newx < len(f[0].strip()) and 0 <= newy < len(f) and f[newy][newx] == '#':
        facing = facings[(facings.index(facing)+1)%4]
    else:
        x = newx
        y = newy
    return x, y, facing

f = open('input.txt', 'r').readlines()
x1 = y1 = 0
for i, line in enumerate(f):
    if '^' in line:
        x1 = line.index('^')
        y1 = i
        break

facing1 = '^'

while 0 <= x1 < len(f[0].strip()) and 0 <= y1 < len(f):
    x1, y1, facing1 = move(x1, y1, facing1)

print(len(seen_old))


seen = []
facings = '^>v<'
def move(x, y, facing, blockx, blocky):

    if [x,y,facing] not in seen:
        seen.append([x,y,facing])
    else:
        return 0, 0, "loop"

    if facing == '^':
        newx = x
        newy = y-1
    elif facing == 'v':
        newx = x
        newy = y+1
    elif facing == '>':
        newx = x+1
        newy = y
    elif facing == '<':
        newx = x-1
        newy = y

    if 0 <= newx < len(f[0].strip()) and 0 <= newy < len(f) and f[newy][newx] == '#' or newy == blocky and newx == blockx:
        facing = facings[(facings.index(facing)+1)%4]
    else:
        x = newx
        y = newy
    return x, y, facing

f = open('input.txt', 'r').readlines()

for i, line in enumerate(f):
    if '^' in line:
        x1start = line.index('^')
        y1start = i
        break

res = 0
for blocky1 in range(len(f)):
    for blockx1 in range(len(f[0].strip())):
        print(blockx1,blocky1)
        if [blockx1,blocky1] not in seen_old or f[blocky1][blockx1] == '#' or blockx1 == x1start and blocky1 == y1start:
            continue

        facing1 = '^'
        x1 = x1start
        y1 = y1start
        seen = []

        while 0 <= x1 < len(f[0].strip()) and 0 <= y1 < len(f):
            x1, y1, facing1 = move(x1, y1, facing1, blockx1, blocky1)
            if facing1 == 'loop':
                res += 1
                break

print(res)

