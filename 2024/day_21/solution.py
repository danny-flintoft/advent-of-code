dir_ = "2024/day_21/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

from collections import deque
import numpy as np
######################### part 1 #########################

directions = {(0,1):'v',
              (0,-1):'^',
              (1,0):'>',
              (-1,0):'<'
              }

keypad_grid = {(0,0):'7',
               (1,0):'8',
               (2,0):'9',
               (0,1):'4',
               (1,1):'5',
               (2,1):'6',
               (0,2):'1',
               (1,2):'2',
               (2,2):'3',
               (1,3):'0',
               (2,3):'A'}

controller_grid = {(1,0):'^',
                   (2,0):'A',
                   (0,1):'<',
                   (1,1):'v',
                   (2,1):'>'}

def move(location,target, grid):
    locations = deque([([],[],location[0],location[1])])
    end = ()
    routes = []
    quickest = np.inf
    while locations:
        route,cells,x,y = locations.popleft()
        if grid[(x,y)] == target:
            if len(route) > quickest:
                break
            routes.append(route+['A'])
            end = (x,y)
            quickest = len(route)
        for d in directions.keys():
            x_ = x+d[0]
            y_ = y+d[1]
            if (x_,y_) in grid.keys() and (x_,y_) not in cells:
                locations.append((route+[directions[d]],cells+[(x_,y_)],x_,y_))
    return routes, end

ans = 0
for row in data:
    location = (2,3)
    shortest_routes = [[]]
    for target in row:
        route, location = move(location, target, keypad_grid)
        shortest_routes = [a+b for a in shortest_routes for b in route]
      
    long_list = [] ## this is all possible shortest routes to achieve the routes above
    for sr in shortest_routes:
        location = (2,0)
        shortest_routes_2 = [[]]
        for target in sr:
            route, location = move(location, target, controller_grid)
            shortest_routes_2 = [a+b for a in shortest_routes_2 for b in route]
        long_list = long_list+shortest_routes_2
    min_length = min(len(l) for l in long_list)    
    long_list = [l for l in long_list if len(l) == min_length]
    
    long_list_2 = [] ## this is all possible shortest routes to achieve the routes above
    for sr in long_list:
        location = (2,0)    
        shortest_routes_3 = [[]]
        for target in sr:
            route, location = move(location, target, controller_grid)
            shortest_routes_3 = [a+b for a in shortest_routes_3 for b in route]
        long_list_2 = long_list_2+shortest_routes_3
    min_length = min(len(l) for l in long_list_2)    
    long_list_2 = [l for l in long_list_2 if len(l) == min_length]

    ans += min_length*int(row[:3])

print("part 1 answer:", ans)      

######################### part 2 #########################

ans = 0
print("part 2 answer:", ans)   