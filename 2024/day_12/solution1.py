dir_ = "2024/day_12/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

from collections import defaultdict
######################### part 1 #########################

## build grid
grid = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        grid[(x,y)] = data[y][x]

## set directions
directions = [(0,-1),(1,0),(0,1),(-1,0)]
        
## track all locations, remove what has been plotted       
locations = set(grid.keys())   

## function for counting walls
## trick for counting walls: record direction a wall is hit from
## all adjacent squares that were hit from same direction can be reduced to 1
def count_walls(perimiter_dict):
    walls = []
    for key in perimiter_dict:
        checklist = perimiter_dict[key]
        while checklist:
            loc = checklist.pop()
            path = [loc]
            while path:
                p = path.pop()
                for i in range(4):
                    d = directions[i]
                    c = (p[0]+d[0],p[1]+d[1])
                    if c in perimiter_dict[key]:
                        path.append(c)
                        perimiter_dict[key].remove(c)
            walls.append(loc)
    return len(walls)

p1_ans = 0
p2_ans = 0
while locations:
    start = locations.pop()
    plant_locations = [start]
    plant = grid[start]  
    area = 1
    perimiter_count = 0 
    perimiter_dict = defaultdict(list)
    checked = [start]
    while plant_locations:
        loc = plant_locations.pop()
        for i in range(4):
            d = directions[i]
            c = (loc[0]+d[0],loc[1]+d[1])
            if c not in checked:
                val = grid.get(c)
                if val == plant:   
                    area += 1
                    plant_locations.append(c)
                    locations.remove(c)
                    checked.append(c)
                else:      
                    perimiter_count += 1 
                    perimiter_dict[i].append(c)
                    
    wall_count = count_walls(perimiter_dict)
    p1_price = area*perimiter_count
    p2_price = area*wall_count
    p1_ans += p1_price
    p2_ans +=p2_price


print("part 1 answer:", p1_ans)
print("part 2 answer:", p2_ans)
