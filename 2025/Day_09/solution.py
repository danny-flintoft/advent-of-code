dir_ = "2025/day_09/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = test_data

positions = [tuple(int(y) for y in x.split(',')) for x in data]

max_area = 0
for i in positions:
    for j in positions:
        area = (abs(i[0]-j[0])+1)*(abs(i[1]-j[1])+1)
        max_area = max(area, max_area)

ans = max_area

print(f"part 1 answer: {ans}")

######################### part 2 #########################

# part 2 doesn't work yet, too tough!

def get_border(p1, p2):
    border = []
    if p2[0] > p1[0]:
        for x in range(p1[0]+1,p2[0]):
            border.append((x, p1[1]))

    elif p2[0] < p1[0]:
        for x in range(p2[0]+1, p1[0]):
            border.append((x, p1[1]))

    elif p2[1] > p1[1]:
        for x in range(p1[1]+1,p2[1]):
            border.append((p1[0], x))

    elif p2[1] < p1[1]:
        for x in range(p2[1]+1,p1[1]):
            border.append((p1[0], x))
    
    border.append(p2)
    return border
    
    
border = [positions[0]]
previous_point = border[-1]

for point in positions[1:]+[positions[0]]:
    border = border + (get_border(previous_point, point))
    previous_point = point

        
p1 = positions[0]
p3 = positions[3]
p2 = (p1[0],p3[1])
p4 = (p3[0],p1[1])

for b in get_border(p1,p2):
    print(b, b in border)


ans = max_area
print(f"part 2 answer: {ans}")
