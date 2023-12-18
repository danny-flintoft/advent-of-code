input_data = open('day_18/input_1.txt', 'r').read().split('\n')
test_data = open('day_18/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
debug = False
data = input_data
instructions = [tuple(d.split("(")[0].split()) for d in data]

direction_dict = {
    'L':(0,-1),
    'R':(0,1),
    'U':(-1,0),
    'D':(1,0)}


## define function to move based on instruction
def move(location):
    direction = direction_dict[instruction[0]]
    distance = int(instruction[1])
    vector = tuple([distance*d for d in direction])
    location = tuple([a+b for a,b in zip(location,vector)])
    vertices.append(location)
    return location

## loop through all instructions
location = (0,0) ## start position
vertices = []
for instruction in instructions: 
    location = move(location)

## print the path    
grid_height = max(i[0] for i in path)
grid_length = max(i[1] for i in path)

if debug:
    grid = []
    for y in range(grid_height+1):
        row = []
        for x in range(grid_length+1):
            if (y,x) in path:
                cell = '#'
            else:
                cell = '.'
            row.append(cell)
        grid.append(''.join(row))
    
    for row in grid:
        print(row) 

## use shoelace formula to calculate area
interior = 0
for i in range(len(vertices)):
    v1 = vertices[i-1]
    v2 = vertices[i]
    interior += (v1[1]*v2[0]) - (v1[0]*v2[1])
interior = abs(interior)/2

## calculate the length of the path (including vertices)
path_len = 0
verts = [(0,0)]+vertices
for i in range(len(verts)-1):
    a_loc = verts[i]
    b_loc = verts[i+1]
    len_ = abs(sum(a-b for a,b in zip(a_loc,b_loc)))
    path_len+= len_
    
## apply pick's theorem
area =  int(interior + (path_len/2) + 1)

print("part 1 answer:", area)

######################### part 2 #########################
data = input_data

## get the instructions
instructions = [d.split("(")[1][1:-1] for d in data]
direction_map = {
    '0':'R',
    '1':'D',
    '2':'L',
    '3':'U'}
direction = [direction_map[i[-1]] for i in instructions]
distance = [int(i[:-1],16) for i in instructions]
instructions = [(a,b) for a,b in zip(direction,distance)]

## loop through all instructions
location = (0,0) ## start position
vertices = []
for instruction in instructions: 
    location = move(location)

## use shoelace formula to calculate area
interior = 0
for i in range(len(vertices)):
    v1 = vertices[i-1]
    v2 = vertices[i]
    interior += (v1[1]*v2[0]) - (v1[0]*v2[1])
interior = abs(interior)/2

## calculate the length of the path (including vertices)
path_len = 0
verts = [(0,0)]+vertices
for i in range(len(verts)-1):
    a_loc = verts[i]
    b_loc = verts[i+1]
    len_ = abs(sum(a-b for a,b in zip(a_loc,b_loc)))
    path_len+= len_
    
## apply pick's theorem
area =  int(interior + (path_len/2) + 1)

print("part 2 answer:", area)