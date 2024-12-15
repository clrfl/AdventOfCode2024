def draw(chart,walls,boxes,robot):
    for i in range(len(chart)):
        for j in range(len(chart[0])):
            if [j, i] in walls:
                print('##', end='')
                continue
            if [j, i] in boxes:
                print('[]', end='')
                continue
            if [j - 0.5, i] in boxes:
                print(']', end='')
                if [j + 0.5, i] in boxes:
                    print('[', end='')
                elif robot == [j + 0.5, i]:
                    print('@', end='')
                else:
                    print('.', end='')
            elif robot == [j, i]:
                print('@', end='')
                if [j + 0.5, i] in boxes:
                    print('[', end='')
                else:
                    print('.', end='')
            else:
                print('.', end='')
                if [j + 0.5, i] in boxes:
                    print('[', end='')
                elif robot == [j + 0.5, i]:
                    print('@', end='')
                else:
                    print('.', end='')
        print('')

def move_vert(dy):
    global robot
    positions_in_motion = [robot]
    boxes_to_move = []

    for working in positions_in_motion:
        if [working[0],working[1]+dy] in walls or [working[0]-0.5,working[1]+dy] in walls:
            return

        if [working[0],working[1]+dy] in boxes:
            if [working[0],working[1]+dy] not in boxes_to_move:
                boxes_to_move.append([working[0],working[1]+dy])
            positions_in_motion.append( [working[0],working[1]+dy])
            positions_in_motion.append( [working[0]+0.5,working[1]+dy])
        elif [working[0] - 0.5, working[1] + dy] in boxes:
            if [working[0] - 0.5, working[1] + dy] not in boxes_to_move:
                boxes_to_move.append([working[0] - 0.5, working[1] + dy])
            positions_in_motion.append( [working[0] - 0.5, working[1] + dy])
            positions_in_motion.append( [working[0], working[1] + dy])

    # if this part is reached, everything is free to move
    robot = [robot[0], robot[1]+dy]
    for item in boxes_to_move:
        boxes.remove(item)
        boxes.append([item[0],item[1]+dy])
    return


def move_horiz(dx):
    global robot
    working = robot
    boxes_to_move = []
    while True:
        working = [working[0]+dx,working[1]]
        if working in walls or [working[0]-0.5,working[1]] in walls:
            break

        if working in boxes:
            boxes_to_move.append(working)
            working = [working[0] + dx, working[1]]
            continue
        elif [working[0]-0.5,working[1]] in boxes:
            boxes_to_move.append([working[0]-0.5,working[1]])
            working = [working[0] + dx, working[1]]
            continue

        else: #elif working not in boxes:
            # found a free spot
            robot = [robot[0]+dx, robot[1]]
            for item in boxes_to_move:
                boxes.remove(item)
                boxes.append([item[0]+dx,item[1]])
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
            walls.append([float(x),float(y)])
        elif chart[y][x] == 'O':
            boxes.append([float(x),float(y)])
        elif chart[y][x] == '.':
            pass
        elif chart[y][x] == '@':
            robot = [float(x),float(y)]

for instr in instructions:
    if instr == '#':
        break
    if instr == '^':
        move_vert(-1)
    elif instr == 'v':
        move_vert(1)
    elif instr == '>':
        move_horiz(0.5)
    elif instr == '<':
        move_horiz(-0.5)



res = 0
for box in boxes:
    res += box[0] * 2 + box[1] * 100

draw(chart, walls, boxes, robot)
print(int(res))