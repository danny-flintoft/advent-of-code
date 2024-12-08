dir_ = "2024/day_08/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

from itertools import combinations  
######################### part 1 #########################
data

## build grid + copy of grid to track antinodes
grid = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        grid[(x,y)] = data[y][x]
antinode_grid = grid.copy()

## get all pairs
pairs = []
for freq in set(grid.values()):
    if freq == '.':
        continue
    locations = []
    for key, value in grid.items():
        if value == freq:
            locations.append(key)
    pairs = pairs + list(combinations(locations,2))
    
## for each pair calculate the distance and subtract/add to each antenna location
for pair in pairs:
    distance = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    antinode_1 = (pair[0][0] - distance[0], pair[0][1] - distance[1])
    antinode_2 = (pair[1][0] + distance[0], pair[1][1] + distance[1])
    antinode_grid[antinode_1] = '#'
    antinode_grid[antinode_2] = '#'

## only count antinides within the initial grid locations
ans = 0
for key, value in antinode_grid.items():
    if key in grid.keys() and value == '#':
        ans += 1
print("part 1 answer:", ans)

######################### part 2 #########################

## for each pair calculate the distance and subtract/add to each antenna location
## for 0 - 100 times the distance
for pair in pairs:
    distance = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])    
    for i in range(100):
        antinode_1 = (pair[0][0] - (distance[0])*i, pair[0][1] - (distance[1])*i)
        antinode_2 = (pair[1][0] + (distance[0])*i, pair[1][1] + (distance[1])*i)
        antinode_grid[antinode_1] = '#'
        antinode_grid[antinode_2] = '#'
  
## only count antinides within the initial grid locations
ans = 0
for key, value in antinode_grid.items():
    if key in grid.keys() and value == '#':
        ans += 1

print("part 2 answer:", ans)
