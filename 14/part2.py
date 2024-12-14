f = open('input.txt', 'r').readlines()
width = 101
height = 103
steps = 1
robots = []
for line in f:
    line = line.strip().split(' ')
    robot = [list(map(int, line[0][2:].split(','))), list(map(int, line[1][2:].split(',')))]
    robots.append(robot)


x_avg_dists = []
y_avg_dists = []
iteration = 0
x_cycle_its = []
y_cycle_its = []

while True:
    iteration += 1
    x_vals = []
    y_vals = []

    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0] * steps) % width
        robot[0][1] = (robot[0][1] + robot[1][1] * steps) % height
        x_vals.append(robot[0][0])
        y_vals.append(robot[0][1])

    x_avg = sum(x_vals) / len(x_vals)
    y_avg = sum(y_vals) / len(y_vals)

    x_avg_dist = 0
    y_avg_dist = 0

    for val in x_vals:
        x_avg_dist += abs(val - x_avg)
    for val in y_vals:
        y_avg_dist += abs(val - y_avg)

    x_avg_dists.append(x_avg_dist)
    y_avg_dists.append(y_avg_dist)

    # find out when x and y value distributions are more than 30% off the average distribution of values
    if len(x_avg_dists) > 0 and abs(1 - (x_avg_dist / (sum(x_avg_dists) / len(x_avg_dists)) )) > 0.3:
        x_cycle_its.append(iteration)
    if len(y_avg_dists) > 0 and abs(1 - (y_avg_dist / (sum(y_avg_dists) / len(y_avg_dists)))) > 0.3:
        y_cycle_its.append(iteration)

    if iteration > 1000:
        break

# x values show anomaly every x_cycle iterations, starting at x_offset, y accordingly. Find out where they meet
x_offset = x_cycle_its[0]
y_offset = y_cycle_its[0]

x_cycle = x_cycle_its[3] - x_cycle_its[2]
y_cycle = y_cycle_its[3] - y_cycle_its[2]

x_its = 1
y_its = 1

while x_cycle * x_its + x_offset != y_cycle * y_its + y_offset:
    if x_cycle * x_its + x_offset < y_cycle * y_its + y_offset:
        x_its += 1
    else:
        y_its += 1


steps = x_cycle * x_its + x_offset
robots = []
for line in f:
    line = line.strip().split(' ')
    robot = [list(map(int, line[0][2:].split(','))), list(map(int, line[1][2:].split(',')))]
    robots.append(robot)
for robot in robots:
    robot[0][0] = (robot[0][0] + robot[1][0] * steps) % width
    robot[0][1] = (robot[0][1] + robot[1][1] * steps) % height

# draw image of tree
if True:
    output = ''
    for i in range(height):
        for j in range(width):
            count = 0
            for robot in robots:
                if robot[0][0] == j and robot[0][1] == i:
                    count += 1
            if count > 0:
                output = output + str(count)
            else:
                output = output + '.'
        output = output + '\n'

    print(output)
print(steps)