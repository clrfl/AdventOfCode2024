def move(dx, dy):
    global robot
    working = robot
    boxes_to_move = []
    while True:
        working = [working[0]+dx,working[1]+dy]
        if working in walls or not (0 <= working[0] < len(chart[0]) and 0 <= working[1] < len(chart)):
            break

        if working in boxes:
            boxes_to_move.append(working)
            continue

        else: #elif working not in boxes:
            # found a free spot
            robot = [robot[0]+dx, robot[1]+dy]
            for item in boxes_to_move:
                boxes.remove(item)
                boxes.append([item[0]+dx,item[1]+dy])
            break

    return

f = open('input.txt', 'r').readlines()
inputbreak = False
chart = []
robot = []
instructions = ''
for line in f:
    if line == '\n':
        inputbreak = True
        continue
    if not inputbreak:
        chart.append(line.strip())
    else:
        instructions = instructions + line.strip()

boxes = []
walls = []
for y in range(len(chart)):
    for x in range(len(chart[y])):
        if chart[y][x] == '#':
            walls.append([x,y])
        elif chart[y][x] == 'O':
            boxes.append([x,y])
        elif chart[y][x] == '.':
            pass
        elif chart[y][x] == '@':
            robot = [x,y]

for instr in instructions:
    if instr == '^':
        move(0,-1)
    elif instr == 'v':
        move(0,1)
    elif instr == '>':
        move(1,0)
    elif instr == '<':
        move(-1,0)

# draw result
if True:
    for i in range(len(chart)):
        for j in range(len(chart[0])):
            if [j,i] in walls:
                print('#', end='')
            elif [j,i] in boxes:
                print('O', end='')
            elif robot == [j,i]:
                print('@', end='')
            else:
                print('.', end='')
        print('')

res = 0
for box in boxes:
    res += box[0] + box[1]*100
print(res)