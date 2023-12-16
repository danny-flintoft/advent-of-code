input_data = open('day_15/input_1.txt', 'r').read()
test_data = open('day_15/test_input.txt', 'r').read()

######################### part 1 #########################
data = input_data
steps = data.split(',')

def hash_algo(step):
    value = 0
    for symbol in step:
        value = ((value+ord(symbol))*17)%256
    return value

ans = sum(hash_algo(step) for step in steps)
print("part 1 answer:", ans)

######################### part 2 #########################
import re
data = input_data
steps = data.split(',')

## define function to split a step into the label & the instruction
def split_step(step):
    if '=' in step:
        a,b = step.split("=")
    else:
        a = step[:-1]
        b = None
    return a,b

## build dict to track box contents
box_dict = dict(zip(range(0,256),[[] for _ in range(0,256)]))

## cycle through inputs
for step in steps:
    label, instruction = split_step(step)
    box = hash_algo(label)
    if not instruction: ## instruction is empty, therefore we are on a '-' instruction
        box_dict[box] = [lens_ for lens_ in box_dict[box] if not re.match(label,lens_)] ## filter out any lens_ that matches the label
    else: ## we are on an '=' instruction
        lens = label+' '+instruction
        if sum(1 for lens_ in box_dict[box] if re.match(label,lens_)) != 0: ## if the lens is already in the box
            lens_index = [i for i, lens_ in enumerate(box_dict[box]) if re.search(label, lens_)][0] ## get index of lens
            box_dict[box][lens_index] = lens ## replace existing lens with new lens
            pass
            ## update the lens number to the new instruction number
        else:
            box_dict[box].append(lens)
    
    ### have an issue where I am not updating an existing lens with the new number
  
focusing_power = 0
for key, value in box_dict.items():
    lens_slot = 1
    for lens_ in value:
        fp = (key+1)*lens_slot*int(re.findall(r'\d+', lens_)[0])
        focusing_power += fp
        lens_slot+=1
        
print("part 2 answer:", focusing_power)






