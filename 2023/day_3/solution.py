input_data = open('day_3/input_1.txt', 'r').read().split('\n')
test_data = open('day_3/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import re
data = input_data
row_len = len(data[0])
flat_data = ''.join(data)
max_len = len(flat_data)

## general approach
# flatten data into 1 line
# use regex to find all number matches
# get indexes of each match, offset by 1 either side, and by the legnth of 1 row in each direction
# this gives the index of the match + all adjacent cells
# get the values in all of these cells
# check if any of them are symbols, if they are, add the matched number to the running count

matches = re.finditer("\d+",flat_data) ## find all numbers  and cycle through them
count=0
for m in matches:
    index_range = list(range(m.start(0)-1,m.end(0)+1)) ## get index of number, +/-1 to check either side
    check_range = [i-row_len for i in index_range] + [i+row_len for i in index_range] + index_range ## offset by 1 row each way
    symbols = ''.join([flat_data[i] for i in check_range if i>-1 and i<max_len]) ## return all cell values
    if len(re.findall("[^0-9.]",symbols)) != 0: ## check for symbols
        count += int(m.group())
print("part 1 answer:", count)

######################### part 2 #########################
data = input_data
row_len = len(data[0])
flat_data = ''.join(data)
max_len = len(flat_data)

## general approach
# flatten data into 1 line
# use regex to find all number matches
# get indexes of each match, offset by 1 either side, and by the legnth of 1 row in each direction
# this gives the index of the match + all adjacent cells
# return the index of any '*' in adjacent cells
# add gear's index + the matched number value to a dictionary (getting list of number values)
# get prod of pairs, and add to running count

## getting geat numbers
matches = re.finditer("\d+",flat_data) ## find all numbers  and cycle through them
gear_dict = dict()
for m in matches:
    index_range = list(range(m.start(0)-1,m.end(0)+1)) ## get index of number, +/-1 to check either side
    check_range = [i-row_len for i in index_range] + [i+row_len for i in index_range] + index_range ## offset by 1 row each way
    gear_index = [i for i in check_range if i>-1 and i<max_len and flat_data[i] =='*'] ## return all cell values
    if gear_index != []:
        ## use setdefault() to generate index with empty list if none exists, then append the matched number
        gear_dict.setdefault(gear_index[0],[]).append(int(m.group())) ############ this could be a problem if 1 number connects to 2 gears

## prodding and counting
count = 0
for key,value in gear_dict.items():
    if len(value) == 2: ## if the gear joins to 2 numbers
        count+=value[0]*value[1] ## get prod and add to count

print("part 2 answer:", count)