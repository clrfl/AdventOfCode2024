def permutate_oplist(oplist2):
    for digit in range(len(oplist2)):
        if oplist2[digit] == '+':
            oplist2 = oplist2[:digit] + '*' + oplist2[digit + 1:]
            break
        elif oplist2[digit] == '*':
            oplist2 = oplist2[:digit] + '|' + oplist2[digit + 1:]
            break
        elif oplist2[digit] == '|':
            oplist2 = oplist2[:digit] + '+' + oplist2[digit + 1:]
            continue
    return oplist2


f = open('input.txt', 'r').readlines()
res = 0
for line in f:
    print(line.strip())
    line = line.strip().split(':')
    result = int(line[0])
    vals = line[1].strip().split(' ')
    vals = list(map(int, vals))

    ops = '+*|'
    oplist = ''
    final_oplist = ''

    for i in range(len(vals) -1):
        oplist = oplist + '+'
        final_oplist = final_oplist + '|'

    while True:
        # apply ops
        temp = vals[0]
        for i in range(len(oplist)):
            if oplist[i] == '+':
                temp = temp + vals[i+1]
            elif oplist[i] == '*':
                temp = temp * vals[i+1]
            elif oplist[i] == '|':
                temp = int(str(temp)+str(vals[i+1]))
            if temp > result:
                break

        # test
        if temp == result:
            res += result
            break
        elif oplist == final_oplist:
            break

        # permutate ops
        oplist = permutate_oplist(oplist)

print(res)

# 52338620733 That's not the right answer; your answer is too low.
