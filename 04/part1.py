def discover_xmas(f, line, col):
    pattern = "XMAS"
    matches = 0
    # right
    ok = 0
    if col < len(f[0].strip()) - len(pattern) + 1:
        for i in range(len(pattern)):
            if f[line][col+i] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # left
    ok = 0
    if col > 0 + len(pattern) - 2:
        for i in range(len(pattern)):
            if f[line][col-i] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # up
    ok = 0
    if line > 0 + len(pattern) - 2:
        for i in range(len(pattern)):
            if f[line-i][col] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # down
    ok = 0
    if line < len(f) - len(pattern) + 1:
        for i in range(len(pattern)):
            if f[line+i][col] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # right-up
    ok = 0
    if col < len(f[0].strip()) - len(pattern) + 1 and line > 0 + len(pattern) - 2:
        for i in range(len(pattern)):
            if f[line-i][col+i] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # right-down
    ok = 0
    if col < len(f[0].strip()) - len(pattern) + 1 and line < len(f) - len(pattern) + 1:
        for i in range(len(pattern)):
            if f[line+i][col+i] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # left-up
    ok = 0
    if col > 0 + len(pattern) - 2 and line > 0 + len(pattern) - 2:
        for i in range(len(pattern)):
            if f[line-i][col-i] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    # left-down
    ok = 0
    if col > 0 + len(pattern) - 2 and  line < len(f) - len(pattern) + 1:
        for i in range(len(pattern)):
            if f[line+i][col-i] == pattern[i]:
                ok += 1
        if ok == len(pattern):
            matches += 1

    return matches

f = open('input.txt', 'r').readlines()
res = 0
for line in range(len(f)):
    for col in range(len(f[line])):
        if f[line][col] == 'X':
            res += discover_xmas(f, line, col)
print(res)

