input_data = open('day_11/input_1.txt', 'r').read().split('\n')
test_data = open('day_11/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import numpy as np ## used to transpose array
from itertools import combinations ## used to get galaxy combos
data = input_data
data = [list(i) for i in data]

## get index of the empty cols and rows
empty_rows = [i for i in range(len(data)) if data[i].count('.') == len(data[i])]
transposed_data = np.transpose(data).tolist()
empty_columns = [i for i in range(len(transposed_data)) if transposed_data[i].count('.') == len(transposed_data[i])]

## index galaxies
expansion = 2 ## volume by which to expand the universe
height = len(data)
length = len(data[0])
i = 0 ## galaxy number
galaxy_dict = {}
for y in range(height):
    row = data[y]
    for x in range(length):
        cell = row[x]
        if cell == '#': ## if it's a galaxy
            y_offset = sum(y > val for val in empty_rows)*(expansion-1)
            x_offset = sum(x > val for val in empty_columns)*(expansion-1)
            galaxy_dict[i] = (y+y_offset,x+x_offset)
            i+=1

## get combos
galaxy_combinations = list(combinations(galaxy_dict.keys(), 2))

## get distances
ans = 0
for galaxy in galaxy_combinations:
    p1 = galaxy_dict[galaxy[0]] ## get position of galaxy 1
    p2 = galaxy_dict[galaxy[1]] ## get position of galaxy 2
    dist = abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) ## find the distance between them
    ans+=dist
print("part 1 answer:", ans)

######################### part 2 #########################
data = input_data

## index galaxies
expansion = 1000000 ## volume by which to expand the universe
height = len(data)
length = len(data[0])
i = 0 ## galaxy number
galaxy_dict = {}
for y in range(height):
    row = data[y]
    for x in range(length):
        cell = row[x]
        if cell == '#': ## if it's a galaxy
            y_offset = sum(y > val for val in empty_rows)*(expansion-1)
            x_offset = sum(x > val for val in empty_columns)*(expansion-1)
            galaxy_dict[i] = (y+y_offset,x+x_offset)
            i+=1

## get combos
galaxy_combinations = list(combinations(galaxy_dict.keys(), 2))

## get distances
ans = 0
for galaxy in galaxy_combinations:
    p1 = galaxy_dict[galaxy[0]] ## get position of galaxy 1
    p2 = galaxy_dict[galaxy[1]] ## get position of galaxy 2
    dist = abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) ## find the distance between them
    ans+=dist

print("part 2 answer:", ans)
