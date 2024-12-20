dir_ = "2024/day_16/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

import numpy as np

######################### part 1 & 2 #########################

## using Dijkstra's Algo

## build grid and find start node
X = len(data[0])
Y = len(data)
grid = {}
for x in range(X):
    for y in range(Y):
        grid[(x,y)] = data[y][x]
        if grid[(x,y)] == 'S':
            start_node = (x,y,0) ## x,y,direction

## define directions
dir_ = [(1,0),(0,1),(-1,0),(0,-1)]

## build graph of nodes and adjacent nodes
def get_adjacent_nodes(node):
    d = dir_[node[2]]    

    next_nodes = [(node[0],node[1],(node[2]+1)%4), ## rotate clockwise
                   (node[0],node[1],(node[2]-1)%4)] ## rotate anti-clockwise
    costs = [1000,1000]
    
    ## only allow move if it's not into a #
    val = grid[(node[0]+d[0],node[1]+d[1])]
    if val != '#':
        next_nodes.append((node[0]+d[0],node[1]+d[1],node[2]))
        costs.append(1)
    return dict(zip(next_nodes,costs))

graph = {}
for key,value in grid.items():
    if value in ['S','.','E']:
        for d in range(4):
            node = (key[0], key[1], d)
            graph[node] = get_adjacent_nodes(node)

## build list of unvisited nodes
unvisited_nodes = list(graph.keys())

## dict to track cost of reaching each node
costs = graph.copy()
for key in costs.keys():
    costs[key] = np.inf
costs[start_node] = 0

## dict to track route taken to reach end node
routes = costs.copy()
for key in routes.keys():
    routes[key] = set()
routes[start_node].add(start_node[:2])

## visit all nodes and work out min costs
while unvisited_nodes:
#for i in range(10):
    ## sort our list of unvisited nodes by min cost to reach
    ## and take node with lowest cost to check next
    unvisited_nodes = sorted(unvisited_nodes, key = costs.get)
    node = unvisited_nodes.pop(0)
    for key,value in graph[node].items():
        ## compare current best vs new cost to reach given node
        current_cost = costs[key]
        new_cost = costs[node] + value
        if new_cost < current_cost:
            ## update best cost
            costs[key] = new_cost
            ## update best route
            routes[key] = routes[node].copy()
            routes[key].add(key[:2])
        elif new_cost == current_cost:
            routes[key] = routes[key].union(routes[node]) 
        
## find min dist to target
min_cost = np.inf
best_key = None
for key,value in costs.items():
    grid_value = grid[(key[0],key[1])]
    if grid_value == 'E' and value < min_cost:
        min_cost = value
        best_key = key
        
ans = min_cost
print("part 1 answer:", ans)

ans = len(routes[best_key])       
print("part 2 answer:", ans)