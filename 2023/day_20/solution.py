input_data = open('day_20/input_1.txt', 'r').read().split('\n')
test_data = open('day_20/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import copy
debug = False
data = input_data

## build dict to track the module (key) and its type, destinations, and starting state (value)
module_dict = {}
for row in data:
    row = row.split(' -> ')
    if row[0] == 'broadcaster':
        module_name = 'broadcaster'
        module_type = 'broadcaster'
        module_state = None
    else:
        module_name = row[0][1:]
        module_type = row[0][0]
        module_state = 0
    module_destinations = row[1].split(', ')
    module_dict[module_name] = [module_type,module_destinations,module_state]

## modify the module_state for the conjunction modules to be a dictoinary of source modules and states
for key,value in module_dict.items():
    if value[0] == '&': ## find the conjunction modules
        key_dict = {}
        for key_,value_ in module_dict.items():
            if key in value_[1]:
                key_dict[key_] = 0
        module_dict[key][2] = key_dict

## some destination modules are not set up as transmitting modules, we need to add these into the module dict still

destination_modules = []
for row in data:
    destination_modules = destination_modules + row.split(' -> ')[1].split(', ')

for module in destination_modules:
    if module in module_dict.keys():
        pass
    else:
        module_dict[module] = [None,None,None]

initial_state_dict = copy.deepcopy(module_dict) ## take a copy of the initial state so we can easily reset to initial states for part 2

## generate pulse queue used to track all the pulses that are currently queued (pulse_state, destination, source)
pulses = [(0,'broadcaster','button')]

## define broadcast function, triggered when a broadcast module receives a pulse
def broadcaster(pulse): 
    pulse_state = pulse[0]
    module_name = pulse[1]
    destinations = module_dict[module_name][1]
    ## transmit pulses
    output_pulses = [(pulse_state,destination,module_name) for destination in destinations]
    for output in output_pulses:
        pulses.append(output)
        
## define flip-flip function, triggered when a flip-flop module receives a pulse
def flip_flop(pulse):
    pulse_state = pulse[0]
    module_name = pulse[1]
    module_state = module_dict[module_name][2]
    destinations = module_dict[module_name][1]
    ## alter flip_flip state
    if pulse_state == 1:
        pass ## nothing happens if a high state pulse is received
    elif pulse_state == 0:
        if module_state == 0:
            module_dict[module_name][2] = 1
            output = 1
        else:
            module_dict[module_name][2] = 0
            output = 0
        ## transmit pulses
        for destination in destinations:
            pulses.append((output,destination,module_name))

## define conjunction function, triggered when a conjunction module receives a pulse
def conjunction(pulse):
    pulse_state = pulse[0]
    module_name = pulse[1]
    pulse_source = pulse[2]
    module_state_dict = module_dict[module_name][2] ## the sources that supply this module
    destinations = module_dict[module_name][1]

    ## update tracked state
    module_state_dict[pulse_source] = pulse_state ## update state dict
    module_dict[module_name][2] = module_state_dict ## update this in the main dic   
    
    ## transmit pulses
    if min(module_state_dict.values()) == 0:
        output = 1
    else: 
        output = 0
    for destination in destinations:
        pulses.append((output,destination,module_name))

## define output function, triggered when an output module receives a pulse
def output(pulse):
    pass 

## run 1000 loops of the process
low_count = 0
high_count = 0
for i in range(1000):
    pulses = [(0,'broadcaster','button')]
    while len(pulses) != 0:
        pulse = pulses.pop(0)  
        
        ## increment pulse count
        if pulse[0] == 0:
            low_count += 1
        else: high_count += 1
        
        ## process pulse
        if pulse[1] == 'output':
            destination_type = 'output'
        else:
            destination_type = module_dict[pulse[1]][0]
        if destination_type == 'broadcaster':
            broadcaster(pulse)
        elif destination_type == '%':
            flip_flop(pulse)
        elif destination_type == '&':
            conjunction(pulse)
        elif destination_type == 'output':
            output(pulse)

ans = (low_count*high_count)
print("part 1 answer:", ans)

######################### part 2 #########################

## reset the dict
module_dict = copy.deepcopy(initial_state_dict)

## after some digging into the data, determined that we need the LMS between the flip-flops fed by the broadcaster being in a state of 0
modules_of_interest = module_dict['broadcaster'][1]

gd_lows = []
kg_lows = []
gt_lows = []
lf_lows = []

for i in range(10000):
    rx_low_count = 0
    rx_high_count = 0
    pulses = [(0,'broadcaster','button')]
    gd_lows.append(module_dict['gd'][2])
    kg_lows.append(module_dict['kg'][2])
    gt_lows.append(module_dict['gt'][2])
    lf_lows.append(module_dict['lf'][2])
    
    while len(pulses) != 0:
        pulse = pulses.pop(0)  
        ## process pulse
        if pulse[1] == 'output':
            destination_type = 'output'
        else:
            destination_type = module_dict[pulse[1]][0]
        if destination_type == 'broadcaster':
            broadcaster(pulse)
        elif destination_type == '%':
            flip_flop(pulse)
        elif destination_type == '&':
            conjunction(pulse)
        elif destination_type == 'output':
            output(pulse)

def pattern_finder(data_set):
    for i in range (1,int(len(data_set)/2)):
        candidate = data_set[:i]
        extended = candidate*int(len(data_set)/len(candidate))
        if extended == data_set[:len(extended)]:
            pattern = candidate
            break
    return pattern
 
m_1 = len(pattern_finder(gd_lows))
m_2 = len(pattern_finder(kg_lows))
m_3 = len(pattern_finder(gt_lows))
m_4 = len(pattern_finder(lf_lows))

import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

lcm_1 = lcm(m_1,m_2)
lcm_2 = lcm(lcm_1,m_3)
lcm_3 = lcm(lcm_2,m_4)

print("part 2 answer:", lcm_3)
    



