a = []
b = []
for line in open('input.txt', 'r').readlines():
    vals = line.strip().split('   ')
    a.append(int(vals[0]))
    b.append(int(vals[1]))

a.sort()
b.sort()
res = 0

for i in range(len(a)):
    res += abs(a[i] - b[i])

print(res)