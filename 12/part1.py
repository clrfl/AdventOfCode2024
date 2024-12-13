def discover(start):
    new_crop = [start]
    crop_type = f[start[0]][start[1]]

    for el in new_crop:
        if el[0] > 0:
            crop_to_discover = [el[0]-1, el[1]]
            if crop_to_discover not in discovered and f[crop_to_discover[0]][crop_to_discover[1]] == crop_type:
                new_crop.append(crop_to_discover)
                discovered.append(crop_to_discover)
        if el[1] > 0:
            crop_to_discover = [el[0], el[1]-1]
            if crop_to_discover not in discovered and f[crop_to_discover[0]][crop_to_discover[1]] == crop_type:
                new_crop.append(crop_to_discover)
                discovered.append(crop_to_discover)
        if el[0] + 1 < len(f):
            crop_to_discover = [el[0] + 1, el[1]]
            if crop_to_discover not in discovered and f[crop_to_discover[0]][crop_to_discover[1]] == crop_type:
                new_crop.append(crop_to_discover)
                discovered.append(crop_to_discover)
        if el[1] + 1 < len(f[0].strip()):
            crop_to_discover = [el[0], el[1] + 1]
            if crop_to_discover not in discovered and f[crop_to_discover[0]][crop_to_discover[1]] == crop_type:
                new_crop.append(crop_to_discover)
                discovered.append(crop_to_discover)
    return new_crop

f = open('input.txt', 'r').readlines()
discovered = []
crops = []

for i in range(len(f)):
    for j in range(len(f[0].strip())):
        if [i,j] not in discovered:
            discovered.append([i,j])
            crops.append(discover([i,j]))

res = 0
for crop in crops:
    perimeter = 0
    for el in crop:
        if [el[0]-1, el[1]] not in crop:
            perimeter += 1
        if [el[0]+1, el[1]] not in crop:
            perimeter += 1
        if [el[0], el[1]-1] not in crop:
            perimeter += 1
        if [el[0], el[1]+1] not in crop:
            perimeter += 1
    res += perimeter * len(crop)


print(res)
