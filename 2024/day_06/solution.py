dir_ = "2024/day_06/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data
    
######################### part 1 #########################

## populate grid as dictionary, & get starting location and direction
direction = (0,-1)
grid = {}
for x in range(len(data[0])):
    for y in range(len(data)):
        grid[(x,y)] = data[y][x]
        if data[y][x] == '^':
            location = starting_location = (x,y)           

## define function to move 1
def move(back=False):
    if back:
        backwards = [-y for y in direction]
        new_location = tuple(sum(x) for x in zip(location, backwards))
    else:   
        new_location = tuple(sum(x) for x in zip(location, direction))
    return new_location

## define function to rotate
def rotate():
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    d = directions.index(direction)
    d = (d+1)%4
    new_direction = directions[d]
    return new_direction

## track visited locations, including starting loc
route = set()
route.add(location)
 
while True:
    location = move()
    if location not in grid:
        break
    elif grid[location] == '#':
        ## move back and rotate clockwise
        location = move(back=True)
        direction = rotate()
    else:
        route.add(location)  
 
ans = len(route)

print("part 1 answer:", ans)

######################### part 2 #########################

## for each step in p1 route, except the starting step, add a '#' and check for loop vs exit
route.remove(starting_location)
ans = 0  
# i=1

for step in route:
    direction = (0,-1)
    location = starting_location
    
    ## add the new block, and remember original cell value to reset after loop
    original_cell = grid[step]
    grid[step] = '#'

    ## run the cycle
    # print(f"check {i} out of {len(route)}")
    # i+=1
    moving = True
    route_p2 = set()
    route_p2.add(str(location) + str(direction))
    
    while True:
        location = move()
        route_step = str(location) + str(direction)
        if location not in grid:
            break
        elif route_step in route_p2:
            ans += 1
            break
        elif grid[location] == '#':
            ## move back and rotate clockwise
            location = move(back=True)
            direction = rotate()
        else:
            route_p2.add(route_step)
            
    ## reset grid
    grid[step] = original_cell

print("part 2 answer:", ans)