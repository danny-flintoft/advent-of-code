input_data = open('day_12/input_1.txt', 'r').read().split('\n')
test_data = open('day_12/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import re
from itertools import permutations, groupby
from sympy.utilities.iterables import multiset_permutations

## import and organise data
data = input_data
records = [i.split()[0] for i in data]
orders = [i.split()[1].split(',') for i in data]

ans = 0
iteration = 1
for record, order in zip(records,orders):
    print("record", iteration,"of",len(records))
    print("record:", record)
    print("order:", order)
    ## get broken part patterns
    broken_part_patterns = []
    for x in [int(i) for i in order]:
        broken_part_patterns.append('.'+''.join(['#']*x)+'.')   
    
    ## get known bits
    # known_sections = list(filter(None,record.split('?')))
    
    ####
    ## for this bit we need to combine what we know, not just have it split into know ### and known ...
    ## e.g. .##, ##., .# etc
    ####
    known_broken = [''.join(['#']*int(i)) for i in order if int(i) > 1]
    known_operational = [i for i in list(filter(None,record.split('?'))) if '#' not in i]
    known = known_broken+known_operational
    
    broken_count = sum(int(i) for i in order)
    known_broken_count = sum(i.count('#') for i in known)
    unknown_broken_count = broken_count - known_broken_count
    
    known_operational_count = sum(i.count('.') for i in known)
    unknown_operational_count = len(record) - known_operational_count - broken_count
    extra_parts = ['#']*unknown_broken_count + ['.']*unknown_operational_count
    all_parts = known+extra_parts
    
    ## we know that any solution must be made up of the known sections, + the extra parts
    ## get all combos of these part, and add a . at either end to allow for parts at start or end of component list
    # variants = set(['.'+''.join(i)+'.' for i in permutations(all_parts)]) ## cast as set to remove duplicates   
    variants = set(['.'+''.join(i)+'.' for i in multiset_permutations(all_parts)]) ## cast as set to remove duplicates   
    
    count = 0
    for variant in variants:
        possible = 1
        
        ## do our broken part patterns appear in the variant
        v = variant
        for pattern in broken_part_patterns:
            l1 = len(v)
            v = v.replace(pattern,'..',1) ## 1 means only replace the first match
            l2 = len(v)
            if l1 == l2:
                possible = 0
        
        ## does the variant match the original mapping?
        pattern = "^"+record.replace(".","\.").replace("?",".")+"$"
        if len(re.findall(pattern,variant[1:-1]))==0:
            possible = 0 
            
        ## does the order match?
        groups = groupby(variant)
        variant_order = [str(sum(1 for _ in group)) for label, group in groups if label == '#']
        if variant_order != order:
            possible = 0
            
        ## count the possible ones
        if possible == 1:
            print("working variant:", variant)
        count+=possible
    
    print(count)
    ans+=count
    iteration+=1

print("part 1 answer:", ans)

######################### part 2 #########################
# data = input_data

# print("part 2 answer:", ans)
