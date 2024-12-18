def up(inpt):
    return [inpt[0], inpt[1]-1]
def down(inpt):
    return [inpt[0], inpt[1]+1]
def left(inpt):
    return [inpt[0]-1, inpt[1]]
def right(inpt):
    return [inpt[0]+1, inpt[1]]
def inbounds(inpt):
    return 0<=inpt[0]<=70 and 0<=inpt[1]<=70

f = open('input.txt', 'r').readlines()

start = [0,0]
end = [70,70]
obstacles = []
queue = [[start,0]]
seen = [start]

for i in range(1024):
    obstacles.append(list(map(int,f[i].strip().split(','))))

for item in queue:
    if item[0] == end:
        print(item[1])
        break

    up1 = up(item[0])
    down1 = down(item[0])
    left1 = left(item[0])
    right1 = right(item[0])

    for el in [up1, down1, left1, right1]:
        if el not in seen and el not in obstacles and inbounds(el):
            queue.append([el,item[1]+1])
            seen.append(el)
