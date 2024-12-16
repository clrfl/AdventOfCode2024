f = open('input.txt', 'r').readlines()
grid = []
end = []
working = []

for y, line in enumerate(f):
    for x, char in enumerate(line.strip()):
        if char == '.':
            grid.append([x,y])
        elif char == 'S':
            working = [[[x,y], [1,0], 0]]
        elif char == 'E':
            end = [x,y]
            grid.append(end)

#working = [[position, facing, price]]
visited = []

while True:

    working.sort(key=lambda x: x[2])
    el = working[0]

    if [el[0],el[1]] in visited:
        del working[0]
        continue

    visited.append([el[0],el[1]])

    if el[0] == end:
        print(el[2])
        break

    if [el[0][0] + el[1][0], el[0][1] + el[1][1]] in grid:
        next_step = [[el[0][0] + el[1][0], el[0][1] + el[1][1]], el[1], el[2]+1]
        if next_step not in working:
            working.append(next_step)

    turn_left = [el[0], [el[1][1], -el[1][0]], el[2] + 1000]
    if [el[0][0]+el[1][1], el[0][1]-el[1][0]] in grid and turn_left not in working:
        working.append(turn_left)

    turn_right = [el[0], [-el[1][1], el[1][0]], el[2] + 1000]
    if [el[0][0]-el[1][1], el[0][1]+el[1][0]] in grid and turn_right not in working:
        working.append(turn_right)

    del working[0]