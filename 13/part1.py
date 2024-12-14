f = open('input.txt', 'r').readlines()
i = 0
ops = []
while i < len(f):
    ops.append([f[i].split(':')[1].strip().split(', '), f[i+1].split(':')[1].strip().split(', '), f[i+2].split(':')[1].strip().split(', ')])
    i += 4
res = 0
for op in ops:
    #   A * ax + B * bx = cx    (I)
    ax = int(op[0][0][2:])
    bx = int(op[1][0][2:])
    cx = int(op[2][0][2:])

    #   A * ay + B * by = cy    (II)
    ay = int(op[0][1][2:])
    by = int(op[1][1][2:])
    cy = int(op[2][1][2:])

    #   A * ax = cx - B * bx
    #   A = cx/ax - bx/ax * B   (I')
    # (I') in (II):
    #   (cx/ax - bx/ax * B) * ay + B * by = cy
    #   ay*cx/ax - ay*bx/ax * B + B * by = cy
    #   ay*cx/ax + B (by - ay*bx/ax) = cy
    #   B * (by - ay*bx/ax) = cy - (ay*cx/ax)
    #   B = (cy - (ay*cx/ax)) / (by - ay*bx/ax)
    b = (cy - (ay*cx/ax)) / (by - ay*bx/ax)
    a = cx / ax - bx / ax * b

    if abs(a-round(a))<0.00000001 and abs(b-round(b))<0.00000001:
        a = int(round(a))
        b = int(round(b))
        if a <= 100 and b <= 100:
            res += a*3+b

print(res)
