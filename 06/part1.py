seen = []
facings = '^>v<'
def move(x, y, facing):
    if [x,y] not in seen:
        seen.append([x, y])

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

print(len(seen))