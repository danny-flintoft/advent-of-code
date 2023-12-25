input_data = open('day_17/input_1.txt', 'r').read().split('\n')
test_data = open('day_17/test_input.txt', 'r').read().split('\n')
test_data_2 = open('day_17/test_input_2.txt', 'r').read().split('\n')

######################### part 1 #########################
import numpy as np
import time
start_time = time.time()
debug = False
progress_readout = False
data = test_data

directions = [(0,1),(0,-1),(1,0),(-1,0)]

# build graph of states, for each position, and possible direct & distance travelled, what are the possible destinations (and costs)
# each node contains 3 bits of info:
## location - the (y,x) grid position
## from_direction - the direction from which we arrived at the grid position
## move - a count of the number of times we have travelled in this direction

graph = {}
y_blacklist = [-1,len(data)]
x_blacklist = [-1,len(data[0])]

for y in range(len(data)):
    for x in range(len(data[0])):
            for from_direction in directions:
                for moves in range(1,4):
                    reverse = (-from_direction[0],-from_direction[1])
                    blacklist = [reverse] ## blacklist the reverse direction. from direction added to this if 3x move limit hit
                    if moves == 3:
                        blacklist.append(from_direction)
                    ## get all adjacent nodes (that aren't blacklisted)
                    adjacent = [(tuple([a+b for a,b in zip((y,x),direction)]),direction) for direction in directions if direction not in blacklist]
                    ## remove any that fall outside the gird
                    adjacent = [x for x in adjacent if x[0][0] not in y_blacklist and x[0][1] not in x_blacklist]
                    ## get direction counts for node info (1 for new directions, or +1 to moves for continued)
                    direction_counts = [moves+1 if i[1] == from_direction else 1 for i in adjacent]
                    next_nodes = [(a[0],a[1],b) for a,b in zip(adjacent,direction_counts)]
                    ## get weights
                    weights = [int(data[a[0][0]][a[0][1]]) for a in adjacent]
                    ## add to graph
                    graph[((y,x),from_direction,moves)] = dict(zip(next_nodes,weights))

## generate list of all unvisited nodes, this is our queue to cycle through
unvisited_nodes = [key for key in graph.keys()]
## generate dictionary to track routes
if debug:
    route_dict = dict(zip(unvisited_nodes,[[] for i in range(len(unvisited_nodes))]))
## generate dictionary to track minimum distance to each node
distance_dict = dict(zip(unvisited_nodes,[np.inf for i in range(len(unvisited_nodes))]))
## set distance for starting node
for key in distance_dict.keys():
    if key[0] == (0,0):
        distance_dict[key]=0

denominator = len(unvisited_nodes)
while unvisited_nodes != []: 
    numerator = len(unvisited_nodes)
    if progress_readout:
        print(f"nodes remaining: {numerator:,} | % completed:{1-(numerator/denominator):.1%}")
    unvisited_nodes = sorted(unvisited_nodes, key=distance_dict.get)
    node = unvisited_nodes.pop(0) ## get unvisited node with lowest distance
    if debug:
        node_route = (route_dict[node]) ## get the route taken to reach node
    if debug:
        print("processing node:",node)
        print("distance to node:",distance_dict[node])
    for key,value in graph[node].items(): 
        ## get best distance taken to reach destination node, + the new distance (and see if the new one is better)
        node_distance = distance_dict[node]
        new_distance = value+node_distance
        best_distance = distance_dict[key]
        if new_distance < best_distance:
            distance_dict[key] = new_distance ## update distance to new best
            if debug:
                route_dict[key] = node_route+[key[1]] ## update route to new route

## find minimum distance
min_dist = np.inf
best_key = None
for key,value in distance_dict.items():
    if key[0] == (len(data)-1,len(data[0])-1):
        if value < min_dist:
            min_dist = value
            best_key = key

## plot best route
if debug:      
    final_route = [(0,0)]
    loc = (0,0)
    for d in route_dict[best_key]:
        loc = tuple([a+b for a,b in zip(loc,d)])    
        final_route.append(loc)
     
    grid = []
    for y in range(len(data)):
        row = []
        for x in range(len(data[0])):
            cell = '.'
            if (y,x) in final_route:
                cell = '#'
            row.append(cell)
        grid.append(row)
        print(row)
    print("")

print("part 1 answer:", min_dist)
print(f"execution time:, {(time.time() - start_time):.1f} seconds")

######################### part 2 #########################
start_time = time.time()
debug = False
progress_readout = True
data = input_data
directions = [(0,1),(0,-1),(1,0),(-1,0)]

graph = {}
y_blacklist = [-1,len(data)]
x_blacklist = [-1,len(data[0])]

y=4
x=10
moves=4
from_direction=(1,0)

for y in range(len(data)):
    for x in range(len(data[0])):
            for from_direction in directions:
                for moves in range(1,11):
                    reverse = (-from_direction[0],-from_direction[1])
                    whitelist = directions.copy()
                    whitelist.remove(reverse)
                    if moves == 10:
                        whitelist.remove(from_direction)
                    if moves<4:
                        whitelist = [from_direction]
                    ## get all adjacent nodes (that aren't blacklisted)
                    adjacent = [(tuple([a+b for a,b in zip((y,x),direction)]),direction) for direction in whitelist]
                    ## remove any that fall outside the gird
                    adjacent = [x for x in adjacent if x[0][0] not in y_blacklist and x[0][1] not in x_blacklist]
                    ## get direction counts for node info (1 for new directions, or +1 to moves for continued)
                    direction_counts = [moves+1 if i[1] == from_direction else 1 for i in adjacent]
                    ## add it all together into the node tuple
                    next_nodes = [(a[0],a[1],b) for a,b in zip(adjacent,direction_counts)]
                    ## remove any where they can't travel 4x in this direction do to hitting end of grid
                    ## does this by projecting out the end location after the 4th movement in that direction
                    for n in next_nodes:
                        n
                        end_position = tuple([x+y for x,y in zip(n[0],(n[1][0]*(4-n[2]),n[1][1]*(4-n[2])))])
                        if end_position[0]<0 or end_position[0]>len(data)-1 or end_position[1]<0 or end_position[1]>len(data[0])-1: ## end position is out of bounds, route not possible
                            next_nodes.remove(n)
                    ## get weights
                    weights = [int(data[a[0][0]][a[0][1]]) for a in adjacent]
                    ## add to graph
                    graph[((y,x),from_direction,moves)] = dict(zip(next_nodes,weights))

## generate list of all unvisited nodes, this is our queue to cycle through
unvisited_nodes = [key for key in graph.keys()]
## generate dictionary to track routes
if debug:
    route_dict = dict(zip(unvisited_nodes,[[] for i in range(len(unvisited_nodes))]))
## generate dictionary to track minimum distance to each node
distance_dict = dict(zip(unvisited_nodes,[np.inf for i in range(len(unvisited_nodes))]))
## set distance for starting node
for key in distance_dict.keys():
    if key[0] == (0,0):
        distance_dict[key]=0

denominator = len(unvisited_nodes)
while unvisited_nodes != []: 
    numerator = len(unvisited_nodes)
    if progress_readout:
        print(f"nodes remaining: {numerator:,} | % completed:{1-(numerator/denominator):.1%}")
    unvisited_nodes = sorted(unvisited_nodes, key=distance_dict.get)
    node = unvisited_nodes.pop(0) ## get unvisited node with lowest distance
    if debug:
        node_route = (route_dict[node]) ## get the route taken to reach node
    if debug:
        print("processing node:",node)
        print("distance to node:",distance_dict[node])
    for key,value in graph[node].items(): 
        ## get best distance taken to reach destination node, + the new distance (and see if the new one is better)
        node_distance = distance_dict[node]
        new_distance = value+node_distance
        best_distance = distance_dict[key]
        if new_distance < best_distance:
            distance_dict[key] = new_distance ## update distance to new best
            if debug:
                route_dict[key] = node_route+[key[1]] ## update route to new route

## find minimum distance
min_dist = np.inf
best_key = None
for key,value in distance_dict.items():
    if key[0] == (len(data)-1,len(data[0])-1):
        if value < min_dist:
            min_dist = value
            best_key = key
 
## plot best route
if debug:      
    final_route = [(0,0)]
    loc = (0,0)
    for d in route_dict[best_key]:
        loc = tuple([a+b for a,b in zip(loc,d)])    
        final_route.append(loc)
     
    grid = []
    for y in range(len(data)):
        row = []
        for x in range(len(data[0])):
            cell = '.'
            if (y,x) in final_route:
                cell = '#'
            row.append(cell)
        grid.append(row)
        print(row)
    print("")

print("part 2 answer:", min_dist)
print(f"execution time:, {(time.time() - start_time):.1f} seconds")