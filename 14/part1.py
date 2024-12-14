f = open('input.txt', 'r').readlines()
width = 101
height = 103
steps = 100
robots = []
for line in f:
    line = line.strip().split(' ')
    robot = [list(map(int, line[0][2:].split(','))), list(map(int, line[1][2:].split(',')))]
    robots.append(robot)

tl = 0
tr = 0
bl = 0
br = 0

for robot in robots:
    robot[0][0] = (robot[0][0] + robot[1][0] * steps) % width
    robot[0][1] = (robot[0][1] + robot[1][1] * steps) % height
    if robot[0][0] < 50:
        if robot[0][1] < 51:
            tl += 1
        elif robot[0][1] > 51:
            bl += 1
    elif robot[0][0] > 50:
        if robot[0][1] < 51:
            tr += 1
        elif robot[0][1] > 51:
            br += 1

print (tl*bl*br*tr)
