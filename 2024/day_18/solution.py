dir_ = "2024/day_18/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data
import numpy as np

######################### part 1 #########################

## Set size of grid, and number of bytes to drop
X=Y=7
bytes_dropped = 12
if len(data) > 25:
    X=Y=71
    bytes_dropped = 1024
start = (0,0)
end = (X-1,Y-1)

## build grid
grid = {}
for x in range(X):
    for y in range(Y):
        if f"{x},{y}" in data[:bytes_dropped]:
            grid[(x,y)] = '#'
        else:
            grid[(x,y)] = '.'

## build graph
directions = [(0,1),(0,-1),(1,0),(-1,0)]
graph = {}
for key, value in grid.items():
    if value == '.':
        adjacent = [(key[0]+d[0],key[1]+d[1]) for d in directions 
                    if grid.get((key[0]+d[0],key[1]+d[1])) == '.']
        graph[key] = adjacent
 
## build costs dict
costs = graph.copy()
for key in costs.keys():
    costs[key] = np.inf
costs[start] = 1

## build routes dict
routes = graph.copy()
for key in routes.keys():
    routes[key] = []
routes[start] = [start]   
 
## run algo   
unvisited = list(graph.keys())
while unvisited:
    unvisited = sorted(unvisited, key = costs.get)
    location = unvisited.pop(0)
    for adjacent in graph[location]:
        current_cost = costs[adjacent]
        new_cost = costs[location]+1
        if new_cost < current_cost:           
            costs[adjacent] = new_cost
            routes[adjacent] = routes[location] + [adjacent]

ans = costs[end]-1
route = routes[end]
print("part 1 answer:", ans)


def plot_grid(grid,on=True):
    if on:
        plot = []
        for y in range(Y):
            row = []
            for x in range(X):
                if (x,y) in route:
                    row.append('O')
                else:
                    row.append(grid[(x,y)])       
            print(''.join(row))
plot_grid(grid) 
       
######################### part 2 #########################
def build_grid(bytes_dropped):
    grid = {}
    for x in range(X):
        for y in range(Y):
            if f"{x},{y}" in data[:bytes_dropped]:
                grid[(x,y)] = '#'
            else:
                grid[(x,y)] = '.'
                
    ## build graph
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    graph = {}
    for key, value in grid.items():
        if value == '.':
            adjacent = [(key[0]+d[0],key[1]+d[1]) for d in directions 
                        if grid.get((key[0]+d[0],key[1]+d[1])) == '.']
            graph[key] = adjacent
 
    ## build costs dict
    costs = graph.copy()
    for key in costs.keys():
        costs[key] = np.inf
    costs[start] = 1
 
    return grid,graph,costs

def run_algo(grid,graph,costs):
    unvisited = list(graph.keys())
    while unvisited:
        unvisited = sorted(unvisited, key = costs.get)
        location = unvisited.pop(0)
        for adjacent in graph[location]:
            current_cost = costs[adjacent]
            new_cost = costs[location]+1
            if new_cost < current_cost:           
                costs[adjacent] = new_cost
                routes[adjacent] = routes[location] + [adjacent]

    ans = costs[end]-1
    return ans

## manually binary searched to find the answer 

bytes_dropped = 3008
grid,graph,costs = build_grid(bytes_dropped)
ans = run_algo(grid,graph,costs)
print(ans)

bytes_dropped = 3009
grid,graph,costs = build_grid(bytes_dropped)
ans = run_algo(grid,graph,costs)
print(ans)

ans = data[bytes_dropped-1]     
print("part 2 answer:", ans)

