input_data = open('day_16/input_1.txt', 'r').read().split('\n')
test_data = open('day_16/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
debug = False
data = input_data

grid_height = len(data)
grid_length = len(data[0])

locations = [(0,-1)] ## start just outside the top left, moving right into cell (0,0)
directions = [(0,1)] ## start moving right, track for all beams

## build dict, to track visited locations (key) and directions they were travelled to from (values)
locations_dict = {}

## define function to move location by 1 in current direction
def move():
    ## move all locations in direction
    deletion = 0
    for i in range(len(locations)):
        i-=deletion ## offsets i to account for locations deleted out of the lists
        locations[i] = tuple([(a+b) for a,b in zip(locations[i],directions[i])])
        if locations[i][0] in [-1,grid_height] or locations[i][1] in[-1,grid_length]:
            ## we are out of bounds, skip this location
            del directions[i]
            del locations[i]
            deletion += 1
            pass
        elif locations[i] in locations_dict.keys(): ## has location been visited already
            if directions[i] in locations_dict[locations[i]]: ## have we visited it from the same direction already            
                del directions[i]
                del locations[i]
                deletion += 1
                pass
            else:
                locations_dict[locations[i]].append(directions[i]) ## add direction to the location key
        else:
            locations_dict.setdefault(locations[i],[]).append(directions[i]) ## add location and direction to dict

def compute_cell(location,direction):
    location_value = data[location[0]][location[1]]
    if debug:
        print(f"location: {location}, cell value: {location_value}")
    if location_value == '.':
        pass
    if location_value == '\\':
        direction = direction[::-1] ## flip the components of the direction    
    if location_value == '/':
        direction = (-direction[1],-direction[0]) ## flip the components & the sign    
    if location_value == '|':
        if direction[1] == 0:   
            ## do nothing if moving horizontally
            pass
        else:
            location = [location,location] ## double location as beam is spilt
            direction = [(1,0),(-1,0)] ## update directions to up and down  
    if location_value == '-':
        if direction[0] == 0:   
            ## do nothing if moving vertically
            pass
        else:
            location = [location,location] ## double location as beam is spilt
            direction = [(0,1),(0,-1)] ## update directions to left and right
    return location, direction

    
## used to flatten direction/location lists where a list contains lists (due to beam split)
def flatten(list_):
    flat_list = []
    for x in list_:
        if type(x) == list:
            flat_list = flat_list + x
        else:
            flat_list.append(x)
    return flat_list
   
while 1 == 1:
    move()
    if debug:
        print(f"locations: {locations}, directions: {directions}")
    new_locations = []
    new_directions = []
    for location, direction in zip(locations,directions):
        new_location, new_direction = compute_cell(location,direction)
        new_locations.append(new_location)
        new_directions.append(new_direction)
    locations = flatten(new_locations) ## update location and direction lists based on cell computation
    directions = flatten(new_directions)
    if len(locations)==0:
        break

ans = len(locations_dict.keys())
print("part 1 answer:", ans)

######################### part 2 #########################
data = input_data

grid_height = len(data)
grid_length = len(data[0])

from_left = [(i,-1) for i in range(grid_height)]
from_right = [(i,grid_length) for i in range(grid_height)]
from_top = [(-1,i) for i in range(grid_length)]
from_bottom = [(grid_height,i) for i in range(grid_length)]

from_left_directions = [(0,1)]*grid_height
from_right_directions = [(0,-1)]*grid_height
from_top_directions = [(1,0)]*grid_length
from_bottom_directions = [(-1,0)]*grid_length

starting_locations = from_left+from_right+from_top+from_bottom
starting_directions = from_left_directions+from_right_directions+from_top_directions+from_bottom_directions

scores = []
i = 0
for starting_location,starting_direction in zip(starting_locations,starting_directions):
    print(f"route {i+1} out of {len(starting_locations)+1}")
    locations_dict = {}
    locations = [starting_location]
    directions = [starting_direction]  
    while 1 == 1:
        move()
        if debug:
            print(f"locations: {locations}, directions: {directions}")
        new_locations = []
        new_directions = []
        for location, direction in zip(locations,directions):
            new_location, new_direction = compute_cell(location,direction)
            new_locations.append(new_location)
            new_directions.append(new_direction)
        locations = flatten(new_locations) ## update location and direction lists based on cell computation
        directions = flatten(new_directions)
        if len(locations)==0:
            break
    scores.append(len(locations_dict.keys()))
    i+=1

ans = max(scores)
print("part 2 answer:", ans)

