f = open('input.txt', 'r').readlines()[0].strip()
templist = []
space = False
idx = 0
for char in f:
    if not space:
        for i in range(int(char)):
            templist.append(str(idx))
        idx += 1
    else:
        for i in range(int(char)):
            templist.append('.')
    space = not space

bwidx = len(templist) - 1
for idx, char in enumerate(templist):
    if char == '.':
        while templist[bwidx] == '.':
            bwidx -= 1
        if bwidx <= idx:
            break
        templist[idx] = templist[bwidx]
        templist[bwidx] = '.'

res = 0
for idx, char in enumerate(templist):
    if char == '.':
        break
    res += idx * int(char)

print(res)