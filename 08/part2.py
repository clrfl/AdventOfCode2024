f = open('input.txt', 'r').readlines()
antennas = []
antinodes = []

for i in range(len(f)):
    for j in range(len(f[0].strip())):
        if f[i][j] != '.':
            antennas.append((i, j, f[i][j]))

for i in range(len(antennas)):
    for j in range(i + 1, len(antennas)):
        if antennas[i][2] == antennas[j][2]:
            a_diff = [antennas[j][0] - antennas[i][0], antennas[j][1] - antennas[i][1]]
            b_diff = [antennas[i][0] - antennas[j][0], antennas[i][1] - antennas[j][1]]

            a = [antennas[i][0] - a_diff[0], antennas[i][1] - a_diff[1]]
            b = [antennas[j][0] - b_diff[0], antennas[j][1] - b_diff[1]]

            while 0 <= a[0] < len(f) and 0 <= a[1] < len(f[0].strip()):
                if a not in antinodes:
                    antinodes.append(a)
                a = [a[0] - a_diff[0], a[1] - a_diff[1]]
            while 0 <= b[0] < len(f) and 0 <= b[1] < len(f[0].strip()):
                if b not in antinodes:
                    antinodes.append(b)
                b = [b[0] - b_diff[0], b[1] - b_diff[1]]

for ant in antennas:
    if [ant[0], ant[1]] not in antinodes:
        antinodes.append([ant[0], ant[1]])

print(len(antinodes))
