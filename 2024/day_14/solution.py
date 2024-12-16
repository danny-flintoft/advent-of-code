dir_ = "2024/day_14/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

import re
from math import sqrt
import numpy as np
######################### part 1 #########################

if len(data) > 12:
    cols = 101
    rows = 103
else:
    cols = 11
    rows = 7

## robot dict, key = velocity, value = position
## some robots have duplicate velocities, so need an id to keep them distinct
robots = {}
id_ = 0
for row in data:
    parsed = re.findall("[0-9-]+",row)
    value = (int(parsed[0]), int(parsed[1]))
    key = (id_, int(parsed[2]), int(parsed[3]))
    robots[key] = value
    id_+=1

def move(velocity, position):
    new_x = (position[0]+velocity[1])%cols
    new_y = (position[1]+velocity[2])%rows
    return (new_x,new_y)

for i in range(100):
    for velocity, position in robots.items():
        robots[velocity] = move(velocity,position)

def count_quadrants(robots):
    q1=q2=q3=q4=0
    for position in robots.values():
        if position[0] < (cols-1)/2:
            if position[1] < (rows-1)/2:
                q1+=1
            elif position[1] > (rows-1)/2:
                q2+=1
        elif position[0] > (cols-1)/2:
            if position[1] < (rows-1)/2:
                q3+=1
            elif position[1] > (rows-1)/2:
                q4+=1
    return q1,q2,q3,q4

q1,q2,q3,q4 = count_quadrants(robots)            
ans = q1*q2*q3*q4
print("part 1 answer:", ans)

######################### part 2 #########################

## robot dict, key = velocity, value = position
## some robots have duplicate velocities, so need an id to keep them distinct
robots = {}
id_ = 0
for row in data:
    parsed = re.findall("[0-9-]+",row)
    value = (int(parsed[0]), int(parsed[1]))
    key = (id_, int(parsed[2]), int(parsed[3]))
    robots[key] = value
    id_+=1
    
## measure average distance to next nearest robot
## when they form a picture I assumet this will be < (1,1)

def get_avg_distance(robots):
    distances = {}
    for key, value in zip(list(robots.keys()),list(robots.values())):
        min_dist = 1000
        for key_2, value_2 in robots.items():
            if key != key_2 and value != value_2: ## not same keys/not same position
                a_dist = abs(value[0]-value_2[0])
                b_dist = abs(value[1]-value_2[1])
                distance = sqrt(a_dist**2+b_dist**2)
                min_dist = min(min_dist,distance)
        distances[key] = min_dist
    avg_distance = sum(distances.values())/len(distances.values())
    return avg_distance
                
iter_ = 0
avg_distances = []
while True:
    for velocity, position in robots.items():
        robots[velocity] = move(velocity,position)
    avg_distance = get_avg_distance(robots)
    avg_distances.append(avg_distance)
    if iter_%1 == 0:
        print(iter_)
    iter_+=1
    if iter_>10000 or avg_distance < 1.5:
        break

## find the iteration with the lowest avg_distance
## this is hopefully the tree???
min_avg_index = np.argmin(avg_distances)
ans = min_avg_index+1
print(min(avg_distances))

## run for the min avg to check
robots = {}
id_ = 0
for row in data:
    parsed = re.findall("[0-9-]+",row)
    value = (int(parsed[0]), int(parsed[1]))
    key = (id_, int(parsed[2]), int(parsed[3]))
    robots[key] = value
    id_+=1
    
for i in range(ans):
    for velocity, position in robots.items():
        robots[velocity] = move(velocity,position)
    
## next need to plot the robots.
plot = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append('.')
    plot.append(row)
    
for p in robots.values():
    plot[p[1]][p[0]] = '#'
    
for row in plot:
    print(''.join(row))
print(iter_)
print(q1,q2,q3,q4)
    
print("part 2 answer:", ans)