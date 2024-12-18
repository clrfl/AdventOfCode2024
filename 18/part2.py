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


def run(obst_count):
    obstacles = []
    for i in range(obst_count):
        obstacles.append(list(map(int,f[i].strip().split(','))))
    queue = [[start,0]]
    seen = [start]
    for item in queue:
        if item[0] == end:
            return item[1]

        up1 = up(item[0])
        down1 = down(item[0])
        left1 = left(item[0])
        right1 = right(item[0])

        for el in [up1, down1, left1, right1]:
            if el not in seen and el not in obstacles and inbounds(el):
                queue.append([el,item[1]+1])
                seen.append(el)
    return ''

upper_bound_success = 2024
lower_bound_fail = len(f)

while lower_bound_fail - upper_bound_success > 1:
    val = int((lower_bound_fail + upper_bound_success) / 2)
    if run(val) == '':
        lower_bound_fail = val
    else:
        upper_bound_success = val

print(f[lower_bound_fail-1])