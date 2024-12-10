dir_ = "2024/day_10/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

######################### part 1 & 2 #########################

## build grid
grid = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        grid[(x,y)] = int(data[y][x])
 
## define possible directions
directions = [(1,0),(0,1),(-1,0),(0,-1)]

p1_ans = 0
p2_ans = 0
for key, value in grid.items():
    if value == 0:
        locations = [(key)]
        p1 = set()
        p2 = 0
        for location in locations:
            new_locations = [tuple(map(sum,zip(location,d))) for d in directions]
            for new_location in new_locations:
                value = grid[location]
                new_value = grid.get(new_location,0)
                if new_value == value + 1:
                    locations.append(new_location)
                    if new_value == 9:
                        p1.add(new_location)
                        p2 += 1
        p1_ans += len(p1)
        p2_ans += p2

print("part 1 answer:", p1_ans)
print("part 2 answer:", p2_ans)
