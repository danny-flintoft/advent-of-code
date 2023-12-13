input_data = open('day_05/input_1.txt', 'r').read().split('\n\n') ## split on double break rather than single this time
test_data = open('day_05/test_input.txt', 'r').read().split('\n\n')

######################### part 1 #########################
data = input_data
data

## get seeds
seeds = [int(i) for i in data[0].split()[1:]]


## build a dictionary for each map, key = int representing map number. value = list of info for each mapping
## could this be better done by building a "map" class? 
map_dict = dict()

i=1 ## running int for the key of our dict, representations the map number by order as they appear in the input
for map_input in data[1:]: ## ignore first line as this is seed info
    for mapping in map_input.split('\n')[1:]: ## split on new line and ignore first item as this is the map name
        mapping = [int(x) for x in mapping.split()] ## split mapping from string into list
        map_range = range(mapping[1],mapping[1]+mapping[2]) ## get range from 2nd & 3rd element of list
        map_offset = mapping[0]-mapping[1] ## calculate offset from 1st & 2nd element of list
        map_info = [map_range,map_offset] ## combine range & offset into a list to append to dict value
        map_dict.setdefault(i,[]).append(map_info) ## add it to the dict
    i+=1

locations = []
for sn in seeds: ##sn = seed_number
    for key, values in map_dict.items():
        for value in values: ## for mapping in map set
            if sn in value[0]: ## if our running value is in the map_range, add the offset and continue to next map set
                sn += value[1]
                break
    locations.append(sn)
    
ans = min(locations)
print("part 1 answer: ", ans)  
## I am amazed this all worked first try!    

######################### part 2 #########################
import ast
data = test_data

## approach is to just track the ranges of values at each mapping stage, converting the max/min of the range

## get seeds 
i=0
starting_seeds=[]
while i < len(seeds):
    tup = (seeds[i],seeds[i]+seeds[i+1]-1)
    starting_seeds.append(tup)
    i+=2

## this function is to compare the seeds, and the mapping ranges, and determine the new 'range' groups based on the overlap
## between the seeds & the map ranges. e.g. seed range of (1,5) and map of (3,5) would result in new seed ranges of (1,2),(3,5)
def match_ranges(starting_seeds, intersects):
    new_seeds = []
    for s in starting_seeds:
        new = list(s)
        for i in intersects:
            if (i[1] <=s[1] and i[1]>=s[0]) and (i[0] >=s[0] and i[0]<=s[1]):            
                new = ([i[1],i[1]+1,i[0],i[0]-1]+list(s))
                new.sort()
            elif (i[1] <=s[1] and i[1]>=s[0]):
                new = ([i[1],i[1]+1]+list(s))
                new.sort()
            elif (i[0] >=s[0] and i[0]<=s[1]):
                new = ([i[0],i[0]-1]+list(s))
                new.sort()
        new=list(zip(new[::2], new[1::2]))
        new_seeds = new_seeds+new 
    return new_seeds

## function to calculate new values based on mapping offset, as done in part 1
def map_func(i,map_i):
    for value in map_dict[map_i]:
            if i in value[0]: ## if i in range
                i+=value[1] ## offset                    
                break
    return i    

## now run through each stage of mapping, applying intersects and offsets
for key in map_dict.keys():
    ## get instersects from map_dict
    intersects=[]
    for i in map_dict[key]:
        tup = ast.literal_eval(str(i[0]).replace("range",""))
        tup = (list(tup)[0],list(tup)[1]-1)
        intersects.append(tup)
    ## find new ranges based on seeds & intersects
    new_seeds = match_ranges(starting_seeds, intersects)
    ## apply offsets
    starting_seeds = [(map_func(i[0],key),map_func(i[1],key)) for i in new_seeds]

ans = min(min(starting_seeds))

print("part 1 answer: ", ans)  
## This however did not work first try!
