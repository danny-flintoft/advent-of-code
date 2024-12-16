dir_ = "2024/day_13/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n\n')
data = input_data

import re
from math import ceil
######################### part 1 #########################

data = [row.split('\n') for row in data]

def build_machine(row):
    machine = {}
    machine['A'] = tuple(int(x) for x in re.findall("[0-9]+",row[0]))
    machine['B'] = tuple(int(x) for x in re.findall("[0-9]+",row[1]))
    machine['P'] = tuple(int(x) for x in re.findall("[0-9]+",row[2]))
    return machine
    
## find all combinations to reach prize
## find max number of A pushes needed and work backwards from there
def process_machine(machine):
    to_hit_x = ceil(machine['P'][0]/machine['A'][0])
    to_hit_y = ceil(machine['P'][1]/machine['A'][1])
    A_presses = min(to_hit_x,to_hit_y)
    B_presses = 0
    
    costs = []
    while A_presses >= 0:
        
        X = (machine['A'][0]*A_presses) + (machine['B'][0]*B_presses)
        Y = (machine['A'][1]*A_presses) + (machine['B'][1]*B_presses)
        
        if (X,Y) == machine['P']:
            cost = (3*A_presses)+(B_presses)
            costs.append(cost)
            A_presses -= 1
            break
        elif X > machine['P'][0] or Y > machine['P'][1]:
            A_presses -= 1
        else:
            B_presses +=1
    return costs, A_presses+1, B_presses

ans = 0
for row in data:
    machine = build_machine(row)
    costs, A_presses, B_presses = process_machine(machine)
    if costs:
        ans += min(costs)

print("part 1 answer:", ans)

######################### part 2 #########################

## solved part 2 using algebra

def build_machine(row):
    add = 10000000000000
    machine = {}
    machine['A'] = tuple(int(x) for x in re.findall("[0-9]+",row[0]))
    machine['B'] = tuple(int(x) for x in re.findall("[0-9]+",row[1]))
    machine['P'] = tuple(int(x)+add for x in re.findall("[0-9]+",row[2]))
    return machine

def process_machine(machine):
    target_X = machine['P'][0]
    target_Y = machine['P'][1]
    A_X_increment = machine['A'][0]
    B_X_increment = machine['B'][0]
    A_Y_increment = machine['A'][1]
    B_Y_increment = machine['B'][1]
    
    A_presses = (target_X - (B_X_increment*target_Y/B_Y_increment)) /\
        (A_X_increment-(B_X_increment*A_Y_increment/B_Y_increment))
    B_presses = (target_Y/B_Y_increment) - (A_presses*A_Y_increment/B_Y_increment)
    if abs(A_presses - round(A_presses)) < 0.001 and abs(B_presses - round(B_presses)) < 0.001: ## accounts for rounding errors with large numbers
        cost = (3*round(A_presses)) + round(B_presses)
        return cost, A_presses, B_presses
    else:
        return 0, A_presses, B_presses
        
ans = 0
for row in data:
    machine = build_machine(row)
    cost, A_presses, B_presses = process_machine(machine)
    ans += cost

print("part 2 answer:", ans)