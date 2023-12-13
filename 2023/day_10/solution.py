input_data = open('day_10/input_1.txt', 'r').read().split('\n')
test_data = open('day_10/test_input.txt', 'r').read().split('\n')
test_data_2 = open('day_10/test_input_2.txt', 'r').read().split('\n')

######################### part 1 #########################
test_run = False
debug = False

if test_run:
    data = test_data_2
else:
    data = input_data

## define dictionary of allowed pipe types for each route (e.g. you can only move up into a | or 7)
directions_dict = {
    (-1,0): ['|','7','F'], ## moving up
    (0,1): ['7','J','-'], ## moving right
    (1,0): ['|','L','J'], ## moving down
    (0,-1): ['F','L','-'], ## moving left
    }

## define dictionary of allowed routes for the given pipe type (e.g. a | can only move up or down)
routes_dict = {
    'F':[(0,1),(1,0)], ## Fs can move right or down
    'J':[(0,-1),(-1,0)], ## Js can move Left or up
    '7':[(0,-1),(1,0)], ## 7s can move left or down
    'L':[(0,1),(-1,0)], ## Ls can move right or up
    '|':[(-1,0),(1,0)], ## |s can move up or 
    '-':[(0,-1),(0,1)] ## -s can move left or right
    }

## define starting location, and pipe type
location = [(i,data[i].index('S')) for i in range(len(data)) if 'S' in data[i]][0]
if test_run:
    pipe = 'F' ## manually inferred from input data
else:
    pipe = '|' ## manually inferred from input data

## define path, which logs the route we have taken so far along the pipe
path = [location]

## define function to move
def move(path,location,pipe):
    if debug:
        print("checking routes: ", routes_dict[pipe])
    for route in routes_dict[pipe]: ## routes the pipe can take
        if debug:
            print("current location: ",location)
            print("attempgin route: ",route)
        check_location = tuple(sum(x) for x in zip(location, route))
        if debug:
            print("checking location: ", check_location)
        if check_location in path:
            if debug:
                print("we have already been here, skip it!\n")
            continue
        if min(list(check_location)) < 0:
            if debug:
                print("we have left the grid, skip it!\n")
            continue
        check_pipe = data[check_location[0]][check_location[1]]
        if debug:
            print("found pipe type: ", check_pipe)
        if check_pipe in directions_dict[route]:
            location = check_location ## move to new location
            pipe = check_pipe
            path.append(location) ## add location to path        
            if debug:
                print("we have moved!\n")
            break ## end loop as we have moved!
        else:
            if debug:
                print("this is an invalid route\n")            
    return path,location,pipe

for i in range(15000): ## not pretty but just going long enough that we know the path will be completed
    if debug:
        print("current path:", path)
        print("current location:", location)
        print("current pipe:", pipe)
    path,location,pipe = move(path,location,pipe)

ans = int(len(path)/2) ## answer would be half the length of the pull path
print("part 1 answer: ", ans)

######################### part 2 #########################

## step 1, extend the path in all directions
## each gap gets filled with the intermediate step, e.g. (0,0) to (0,2) gets filled with (0,1)
long_path = [(i[0]*2,i[1]*2) for i in path]
new_path = []
path_i = 0
for i in range((len(path)*2)-1):
    if i%2==0:
        new_path.append(long_path[path_i]) ## add the actual pipe in
        path_i+=1 ## and move on to the next pipe to be added
    else:
        previous = long_path[path_i-1]
        next_ = long_path[path_i]
        new_pipe = tuple([int(sum(i)/2) for i in zip(previous,next_)])
        new_path.append(new_pipe)

## this doesn't handle going from end of path back to start, below line adds that in
previous = long_path[0]
next_ = long_path[-1]
new_pipe = tuple([int(sum(i)/2) for i in zip(previous,next_)])
new_path.append(new_pipe)

## step 2 expand grid in all directions, adding universal pipe '*'
row_len = len(data[0])
new_grid = []
row_i = 0
for i in range((len(data*2)-1)):
    if i%2 == 0:
        row = data[row_i]
        new_row = ''.join([row[int(i/2)] if i%2==0 else '*' for i in range((row_len*2)-1)]) ## extend row
        row_i += 1
    else:
        new_row = ''.join(['*' for i in range(row_len*2-1)])
    new_grid.append(new_row)

## step 3 plot pipe vs space on grid
grid_height = len(new_grid)
grid_length = len(new_grid[0])
filled_grid = []
for i in range(grid_height):
    new_row = []
    for x in range(grid_length):
        if (i,x) in new_path:
            cell = '.'
        elif i%2 + x%2 == 0:
            cell = '0'
        else:
            cell = '#'
        new_row.append(cell)
    filled_grid.append(''.join(new_row))

## . signifies path, 0 signifies an original non path cell, # signifies new expanded cell    

## step 4, use fill algo on each 0 cell to attempt to reach the edfe of the grid
## that is a cell with index of 0/grid heigh/grid length

sp = (12,4) ## start_point

cells_to_check = [(y,x) for y in range(grid_height) for x in range(grid_length) if filled_grid[y][x] == '0' and y*x != 0]
print("cells to check:", len(cells_to_check))

enclosed_list = []
escaped_list = []
escape_cells_y = [0,grid_height] ## if xval is one of these we have hit grid wall
escape_cells_x = [0, grid_length] ## if xval is one of these we have hit grid wall
for sp in cells_to_check:
    print("checking cell",sp)
    print(f"checking cell {cells_to_check.index(sp)} out of {len(cells_to_check)}")
    location = sp
    visited_locations = [sp]
    black_list = []
    escaped = 0
    stuck = 0
    while 1==1:
        vl_len = len(visited_locations)
        for location in visited_locations:
            #print("total locations visited:",len(visited_locations))
            for route in directions_dict.keys():
                new_location = tuple(sum(x) for x in zip(location, route))
                if new_location[0] < 0 or new_location[0] >= grid_height or new_location[1] < 0 \
                    or new_location[1] >= grid_length or new_location in black_list or new_location in visited_locations:
                    continue ## we left the grid or hit the blacklist or revisited a location so skip past
                new_cell = filled_grid[new_location[0]][new_location[1]]
                if new_location in enclosed_list:
                    stuck = 1
                    break 
                if new_cell == '.':
                    black_list.append(new_location) ## we hit the pipe, add to blacklist
                elif new_location[0] in escape_cells_y or new_location[1] in escape_cells_x \
                    or new_location in escaped_list:
                    escaped = 1 ## we escaped
                    break ## break the loop, we escaped.
                else:
                    visited_locations.append(new_location) ## we visited a new_location
            if escaped==1 or stuck == 1:
                break
        if escaped==1: ## we have escaped, so break the loop for this sp
            print("we escaped")
            escaped_list.append(sp)
            break 
        if stuck == 1 or vl_len == len(visited_locations): ## we have not visited any new spots, we must be stuck in the pipe
            print("we are stuck")
            enclosed_list.append(sp) ## add this sp to our list of enclosed cells
            break ## end search for this sp
                       
ans = len(enclosed_list)
print("part 2 answer:", ans)
