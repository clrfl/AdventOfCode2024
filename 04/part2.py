def discover_xmas(f, line, col):
    if col == 0 or col == len(f[0].strip())-1 or line == 0 or line == len(f)-1:
        return False

    rd = []
    ru = []
    rd.append(f[line-1][col-1])
    rd.append(f[line+1][col+1])
    ru.append(f[line-1][col+1])
    ru.append(f[line+1][col-1])

    if "M" in rd and "S" in rd and "M" in ru and "S" in ru:
        return True

f = open('input.txt', 'r').readlines()
res = 0
for line in range(len(f)):
    for col in range(len(f[line])):
        if f[line][col] == 'A':
            res += 1 if discover_xmas(f, line, col) else 0
print(res)

