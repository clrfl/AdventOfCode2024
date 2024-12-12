f = open('input.txt', 'r').readlines()[0].strip()
templist = []
space = False
idx = 0
for char in f:
    if not space:
        templist.append([int(char), str(idx)])
        idx += 1
    else:
        templist.append([int(char), '.'])
    space = not space

bwidx = len(templist)
while bwidx > 0:
    bwidx -= 1
    if templist[bwidx][1] == '.':
        continue

    size = templist[bwidx][0]
    for i in range(bwidx):
        if templist[i][1] == '.' and templist[i][0] >= size:

            if templist[i][0] - size > 0:
                templist.insert(i, templist[bwidx])
                templist[bwidx + 1] = [size, '.']
                templist[i+1][0] = templist[i+1][0] - size
                bwidx += 1
            else:
                templist[i] = templist[bwidx]
                templist[bwidx] = [size, '.']
            break

res = 0
counter = 0
for val in templist:
    for i in range(int(val[0])):
        if val[1] != '.':
            res += counter * int(val[1])
        counter += 1

print(res)
