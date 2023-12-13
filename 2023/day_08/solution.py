input_data = open('day_08/input_1.txt', 'r').read().split('\n')
test_data = open('day_08/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import re
data = input_data
data

## get directions
directions = [0 if i == 'L' else 1 for i in data[0]]
dir_len = len(directions)

## build out network dict
networks = data[2:]
network_dict = dict()
for n in networks:
    key,value = n.split(" = ")
    value = re.sub("[() ]","",value).split(",")
    network_dict[key]=value

## define naviation function for taking new location from network dict
def navigate(dir_i,location):
    direction = directions[dir_i]
    location = network_dict[location][direction]   
    return location

## get loopy
location = 'AAA'
dir_i = 0 ## iterate over the directions
counter = 0 ## count number of steps
while location != 'ZZZ':
    location = navigate(dir_i,location)
    counter+=1
    dir_i += 1
    if dir_i==dir_len:
        dir_i = 0

print("part 1 answer: ", counter)

######################### part 2 #########################
test_data = open('day_08/test_input_2.txt', 'r').read().split('\n')
data = input_data

## after a bit of exploration I stumbled across a few pieces of info
## 1. each starting location only corresponds to 1 'Z' location
## 2. each starting location hits this Z location at a set interval
## demo'd below

starting_locations = [i for i in network_dict.keys() if i[2]=='A']

location = starting_locations[0] ## begin with the first start location
dir_i = 0 
z_index_list = [] ## track a list of indexes where the end criteria ('Z') is met
z_locations = [] ## track the list of end locations (locations ending with 'Z')
for i in range(1,500000):
    location = navigate(dir_i,location)
    if location[2]=='Z':
        z_index_list.append(i)
        z_locations.append(location)
    i+=1
    dir_i += 1
    if dir_i==dir_len:
        dir_i = 0
        
print(z_index_list)
print(set(z_locations))

## only 1 location is visited, at set intervals (in this case of 15871)
## not shown but this hold true for all locations
## now we know this, we can find all interval values and find the least common multiple

## use this look to get the first index that works
def navigate_loop(location):
    dir_i = 0
    i = 0
    while 1==1:
        location = navigate(dir_i,location)
        if location[2]=='Z':
            break
        i+=1 ## increment i
        dir_i += 1 ## increment direction (or reset)
        if dir_i==dir_len:
            dir_i = 0
    return i ## output the occurence of the first z

z_positions = []
for location in starting_locations:
    pos_1 = navigate_loop(location)+1 ## find first z location
    z_positions.append(pos_1)
    
## now find least common multiple of these, I don't know if there is a pre built algorithm for this but I will try by hand
## my approach is to find the lowest common multiple between location 1 & 2,then between this value and loc 3, then that and loc 4 etc

common_number = z_positions[0] ## the interval for location 1 is our first common_number
for divisor in z_positions[1:]: ## skip the first one because we know the 'common multiple' here is the first value
    check = False ## this will be used to end the loop once check criteria is met
    i = 1 ## used to loop
    while check != True: ## break when check is true
        test_position = common_number*i ## test position is our common number * i
        check = test_position%divisor == 0 ## if test position is divisible by current divisor, criteria is met
        i+=1    
    common_number = test_position ## update our common numbers to the latest test position

print("part 2 answer: ", common_number)
