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
            a = [antennas[i][0] * 2 - antennas[j][0], antennas[i][1] * 2 - antennas[j][1]]
            b = [antennas[j][0] * 2 - antennas[i][0], antennas[j][1] * 2 - antennas[i][1]]
            if a not in antinodes and 0 <= a[0] < len(f) and 0 <= a[1] < len(f[0].strip()):
                antinodes.append(a)
            if b not in antinodes and 0 <= b[0] < len(f) and 0 <= b[1] < len(f[0].strip()):
                antinodes.append(b)

print(len(antinodes))

