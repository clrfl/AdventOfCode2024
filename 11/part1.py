def update(input):
    new = []
    for e in input:
        if e == 0:
            new.append(1)
        elif len(str(e)) % 2 == 0:
            half = int(len(str(e))/2)
            new.append(int(str(e)[:half]))
            new.append(int(str(e)[half:]))
        else:
            new.append(e*2024)
    return new

f = open('input.txt', 'r').readlines()[0].strip().split(' ')
f = list(map(int, f))

for i in range(25):
    f = update(f)

print(len(f))
