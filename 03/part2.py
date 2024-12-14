import re

x = re.findall('mul\\(\\d+,\\d+\\)|do\\(\\)|don\'t\\(\\)', open('input.txt', 'r').read())
res = 0
on = True
for i in x:
    if i == 'do()':
        on = True
        continue
    if i == "don't()":
        on = False
        continue
    if on:
        i = i[4:-1].split(',')
        res += int(i[0]) * int(i[1])
print(res)


