dir_ = "2025/day_03/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

import numpy as np

data = input_data

def get_joltage(bank, digits, current_pos, joltage, current_digit):
    
    # find the block of potential batteries for this digit
    end_of_block = -(digits-1-current_digit)
    if end_of_block > -1:
        block = bank[current_pos:]
    else:
        block = bank[current_pos:end_of_block]
    
    # find the position and value of the highest number in the block
    pos_in_block = np.argmax(block)
    digit_value = str(block[pos_in_block])
    current_pos = pos_in_block + current_pos + 1
    
    # add the new digit to our joltage
    joltage = joltage + digit_value
    
    # return joltage if we are finished, or call the function again
    if len(joltage) == digits:
        return joltage
    else:
        current_digit += 1
        return get_joltage(bank, digits, current_pos, joltage, current_digit)
    

######## part 1 ########

ans = 0
for bank in data:
    
    bank = [int(b) for b in bank]
    joltage = get_joltage(bank, 2, 0, '', 0)
    ans += int(joltage)
    
print(f"part 1 answer: {ans}")

######## part 2 ########

ans = 0
for bank in data:
    
    bank = [int(b) for b in bank]
    joltage = get_joltage(bank, 12, 0, '', 0)
    ans += int(joltage)
    
print(f"part 2 answer: {ans}")







