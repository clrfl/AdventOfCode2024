import re
x = re.findall('mul\\(\\d+,\\d+\\)', open('input.txt', 'r').read())
res = 0
for i in x:
    i = i[4:-1].split(',')
    res += int(i[0]) * int(i[1])
print(res)