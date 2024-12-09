from math import floor
def fix(instruction, rules):
    done = False
    while not done:
        done = True
        for rule in rules:
            if rule[0] in instruction and rule[1] in instruction and instruction.index(rule[0]) > instruction.index(rule[1]):
                a = instruction.index(rule[0])
                b = instruction.index(rule[1])
                inst_a = instruction[a]
                inst_b = instruction[b]
                instruction[a] = inst_b
                instruction[b] = inst_a
                done = False
                break
    return instruction

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
    if not valid:
        fixed = fix(instruction, rules)
        res += int(fixed[floor(len(fixed)/2)])

print(res)
