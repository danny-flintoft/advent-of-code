input_data = open('day_13/input_1.txt', 'r').read().split('\n\n')
test_data = open('day_13/test_input.txt', 'r').read().split('\n\n')

######################### part 1 #########################
import numpy as np
debug = False
data = input_data
data = [d.split('\n') for d in data]

## define function to print our the grid
def print_grid():
    if debug:
        for x in a:
            print(x)
        print("")
        
## define function that transposes our array
def transpose_array():
    array = np.array([list(row) for row in a])
    array = np.array([list(row) for row in a]).transpose()
    array = [''.join(row) for row in array]
    return array

def get_score(score=0,defect_target=0): ## checks mirror at given index and returns a score if there is a mirror match
    ## get mirrored sides
    a_side = a[:i]
    a_len = len(a_side)
    b_side = a[i:i+a_len][::-1] ## take b_side to be as long as a_side, and reverse
    b_len = len(b_side)
    a_side = a_side[a_len-b_len:]
    ## count number of mismatches (defects)
    defects =  sum(sum(x!=y for x,y in zip(a,b)) for a,b in zip(a_side,b_side)) 
    if defects == defect_target: ## if it is mirrored
        score = a_len*o ## if orientation is flipped multiplies score by 100 rather than 1  
    return score 
    
score = 0
for a in data:
    print_grid()
    o=100       
    for i in range(len(a)):
        score += get_score()
        
    ## transpose and repeat
    a = transpose_array()
    o=1
    for i in range(len(a)):
        score += get_score() 

print("part 1 answer:", score)

######################### part 2 #########################
data = input_data
data = [d.split('\n') for d in data]

score = 0
for a in data:
    print_grid()
    o=100       
    for i in range(len(a)):
        score += get_score(defect_target=1)
        
    ## transpose and repeat
    a = transpose_array()
    o=1
    for i in range(len(a)):
        score += get_score(defect_target=1) 
    
print("part 2 answer:", score)