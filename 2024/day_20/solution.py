dir_ = "2024/day_20/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

import numpy as np
from collections import defaultdict
######################### part 1 #########################

## use Dijkstra's forwards & backwards, sum of time to reach any '#' is the cheat time

X = len(data[0])
Y = len(data)
grid = {}
for x in range(X):
    for y in range(Y):
        grid[(x,y)] = data[y][x]
        if data[y][x] == 'S':
            start_position = (x,y) ## third value tracks if the cheat has been used
        if data[y][x] == 'E':
            end_position = (x,y)

directions = [(0,1),(0,-1),(1,0),(-1,0)]

## build graph of states, 3rd value tracks if the cheat has been used (1) or not (0)
graph = {}
for key, value in grid.items():
    if value == '#':
        graph[key] = []
    else:
        adjacent = [(key[0]+d[0],key[1]+d[1]) for d in directions]
        graph[key] = adjacent

## dict of costs (running from S to E and E to S)
costs_forwards = graph.copy()
costs_backwards = graph.copy()
for key in costs_forwards.keys():
    costs_forwards[key] = np.inf
    costs_backwards[key] = np.inf
costs_forwards[start_position] = 0
costs_backwards[end_position] = 0


## run forwards
unvisited = list(costs_forwards.keys())
while unvisited:
    unvisited = sorted(unvisited, key = costs_forwards.get)
    node = unvisited.pop(0)
    for new_node in graph[node]:
        current_cost = costs_forwards[new_node]
        new_cost = costs_forwards[node]+1
        if new_cost < current_cost:
            costs_forwards[new_node] = new_cost

## run backwards
unvisited = list(costs_backwards.keys())
while unvisited:
    unvisited = sorted(unvisited, key = costs_backwards.get)
    node = unvisited.pop(0)
    for new_node in graph[node]:
        current_cost = costs_backwards[new_node]
        new_cost = costs_backwards[node]+1
        if new_cost < current_cost:
            costs_backwards[new_node] = new_cost

quickest_standard = costs_forwards[end_position]

time_saved_dict = defaultdict(int)
for key in costs_forwards.keys():
    alt_speed = costs_forwards[key] + costs_backwards[key]
    time_saved = quickest_standard-alt_speed
    if time_saved > 0:
        time_saved_dict[time_saved] +=1


ans = sum(v for k,v in time_saved_dict.items() if k >= 100)
print("part 1 answer:", ans)  


######################### part 2 ######################### 

iter_ = 1
total = len(costs_forwards.keys())
time_saved_dict = defaultdict(int)
for key_a, cost_a in costs_forwards.items():
    print(f"{iter_} out of {total}")
    iter_+=1
    for key_b, cost_b in costs_backwards.items():
        if key_a != key_b and grid[key_a] in ['E','S','.'] and grid[key_b] in ['E','S','.']:
            manhattan = abs(key_a[0]-key_b[0]) + abs(key_a[1]-key_b[1])
            if manhattan <= 20:
                alt_speed = cost_a + cost_b + manhattan
                time_saved = quickest_standard - alt_speed
                if time_saved > 0:
                    time_saved_dict[time_saved] += 1

ans = sum(v for k,v in time_saved_dict.items() if k >= 100)
print("part 2 answer:", ans)
