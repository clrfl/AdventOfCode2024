from math import floor
f = open('input.txt', 'r').readlines()
i = 0
rules = []
instructions = []
while f[i].strip() != '':
    rules.append(f[i].strip().split('|'))
    i+=1
i+=1
for i in range(i,len(f)):
    instructions.append(f[i].strip().split(','))

res = 0
for instruction in instructions:
    valid = True
    for rule in rules:
        if rule[0] in instruction and rule[1] in instruction and instruction.index(rule[0]) > instruction.index(rule[1]):
            valid = False
            break
    if valid:
        res += int(instruction[floor(len(instruction)/2)])

print(res)