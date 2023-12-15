input_data = open('day_14/input_1.txt', 'r').read().split('\n')
test_data = open('day_14/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import numpy as np
data = test_data
array = np.array([list(x) for x in data])
array = np.rot90(array,axes=(1,0))

def shift_rocks(row):
    row = ''.join(row)
    row = '#'.join([''.join(sorted(x)) for x in row.split('#')])
    row = list(row)
    return row

def index_rocks(row):
    return sum(i+1 for i in np.where(row == 'O')[0]) ## +1 as scoring system starts from 1, not 0   

score = 0
for i in range(len(array)):
    array[i] = shift_rocks(array[i])
    score += index_rocks(array[i])
     
print("part 1 answer:", score)

######################### part 2 #########################

import numpy as np
import matplotlib.pyplot as plt
data = input_data
array = np.array([list(x) for x in data])

scores = [] ## track scores after each cycle
print("performing 500 cycles...")
for iter_ in range(500): ## 3 cycles
    ## perform cycle
    for _ in range(4): ## 4 rotations in a cycle
        array = np.rot90(array,axes=(1,0))
        for i in range(len(array)):
            array[i] = shift_rocks(array[i])
            
    ## get score
    score = 0
    score_array = np.rot90(array,axes=(1,0)) ## need to rotate the array for scoring, but not the main one or it will mess up cycles
    for row in score_array:
        score += index_rocks(row)
    scores.append(score)

## scores follow a specific pattern, we can use this to estimate the score at i = 1000000000
plt.plot(scores[200:]) ## pattern only starts after an initial ramp up so I am skipping to index 200

## find the repeating pattern
## this logic only works if the pattern doesn't repeat any numbers at either end, which seems to be the case
sample_indexes = scores[200:]
for i in range(1,len(sample_indexes)):
    pattern = sample_indexes[:i]
    if set(pattern) == set(sample_indexes): ## pattern is found
        break

plt.plot(scores[200])
plt.plot(pattern)

length_of_pattern = len(pattern)
matching_index = 200+(1000000000-200)%length_of_pattern ## starting from 200, waht would be the remainger when looping to 1 billion
ans = scores[matching_index-1] ## offset by 1 because starts at 0 not 1

print("part 1 answer:", ans)





