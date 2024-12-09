a = []
b = []
for line in open('input.txt', 'r').readlines():
    vals = line.strip().split('   ')
    a.append(int(vals[0]))
    b.append(int(vals[1]))

a.sort()
b.sort()
res = 0

for i in a:
    res += i * b.count(i)
print(res)