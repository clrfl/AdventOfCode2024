def update(input):
    new = {}
    for e in input:
        if e == 0:
            new[1] = new.get(1, 0) + input[e]

        elif len(str(e)) % 2 == 0:
            half = int(len(str(e))/2)
            new[int(str(e)[:half])] = new.get(int(str(e)[:half]), 0) + input[e]
            new[int(str(e)[half:])] = new.get(int(str(e)[half:]), 0) + input[e]
        else:
            new[e * 2024] = new.get(e*2024, 0) + input[e]

    return new

f = open('input.txt', 'r').readlines()[0].strip().split(' ')
f = list(map(int, f))

stones = {}
for el in f:
    stones[el] = stones.get(el, 0) + 1

for i in range(75):
    stones = update(stones)

res = 0
for e in stones:
    res += stones[e]

print(res)