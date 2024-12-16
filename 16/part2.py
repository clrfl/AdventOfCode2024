f = open('input.txt', 'r').readlines()
grid = []
end = []
working = []
links = []
final_el = []
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
        tiles = [el]
        break

    if [el[0][0] + el[1][0], el[0][1] + el[1][1]] in grid:
        next_step = [[el[0][0] + el[1][0], el[0][1] + el[1][1]], el[1], el[2]+1]
        if next_step not in working:
            working.append(next_step)
        links.append([next_step, el])

    turn_left = [el[0], [el[1][1], -el[1][0]], el[2] + 1000]
    if [el[0][0]+el[1][1], el[0][1]-el[1][0]] in grid:
        if turn_left not in working:
            working.append(turn_left)
        links.append([turn_left, el])

    turn_right = [el[0], [-el[1][1], el[1][0]], el[2] + 1000]
    if [el[0][0]-el[1][1], el[0][1]+el[1][0]] in grid:
        if turn_right not in working:
            working.append(turn_right)
        links.append([turn_right, el])

    del working[0]

for tile in tiles:
    for link in links:
        if link[0] == tile:
            tiles.append(link[1])

unique_tiles = []
for tile in tiles:
    if tile[0] not in unique_tiles:
        unique_tiles.append(tile[0])

print(len(unique_tiles))
