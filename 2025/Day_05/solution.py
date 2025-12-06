dir_ = "2025/day_05/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n\n')

######################### part 1 #########################
data = input_data

ranges = data[0].split('\n')
ids = [int(i) for i in data[1].split('\n')]

ranges_dict = dict()
for r in ranges:
    start, end = [int(x) for x in r.split('-')]
    
    if start in ranges_dict.keys(): # there are some duplicate starts, make sure we take the max end of the range
        ranges_dict[start] = max(end, ranges_dict[start])
    else:   
        ranges_dict[start] = end

ans = 0
for i in ids:
    pos_starts = [start for start in ranges_dict.keys() if i >= start]
    
    for pos_start in pos_starts:
        if i <= ranges_dict[pos_start]:
            ans += 1
            break


print(f"part 1 answer: {ans}")

######################### part 2 #########################

## not very interpretable code below, but basically we assess each range once at a time
## if the range overlaps with an existing range at all we take appropriate action
## update the start/end of an existing range, or remove a swallowed range
#### special consideration for if two ranges are modified by one new range, that would cause them to overlap
## if the new range is already within an existing range entirely, do nothing
## else, add the new range

ranges_dict = dict()
for r in ranges:
    
    fix = 0
    start, end = [int(x) for x in r.split('-')]    
    print("assessing range",r)
    
    ## if this absorbs any ranges, delete those ranges
    to_delete = [s for s,e in ranges_dict.items() if s >= start and e <= end]
    for s in to_delete:
        print(f"deleteing range {s}:{ranges_dict[s]}")
        del ranges_dict[s]    
    
    ## if end is > an existing end, and start is <= existing end, update the existing end
    shortlist = [ee for ee in ranges_dict.values() if end > ee and start <= ee]
    if len(shortlist) > 0:
              
        old_end = shortlist[0]
        existing_start = list(ranges_dict.keys())[list(ranges_dict.values()).index(old_end)]
        
        ranges_dict[existing_start] = end
        fix = 1
        print('changing end')
    
    ## if start is < an existing start, and end is >= existing start, update the existing start
    shortlist = [es for es in ranges_dict.keys() if start < es and end >= es]
    if len(shortlist) > 0:
        old_start = shortlist[0]
        new_end = max(end, ranges_dict[old_start])
        
        # if we already amended an end, we have an overlap between 2 existing ranges
        if fix == 1:
            del ranges_dict[old_start]
            ranges_dict[existing_start] = new_end
            
        else:
            del ranges_dict[old_start]
            ranges_dict[start] = new_end
            fix = 1
            print('changing start')
     
    ## if absorbed by an existing range do nothing
    lower_starts = [s for s in ranges_dict.keys() if s <= start]
    larger_ends = [ranges_dict[s] for s in lower_starts if ranges_dict[s] >= end]
    
    if len(larger_ends) > 0 and fix == 0:
        print("contained by existing range")
    elif fix == 0:
        ranges_dict[start] = end
        print("add as new range")
    
    print(ranges_dict)
    print()
    
ans = sum(e-s+1 for s,e in ranges_dict.items())
    
print(f"part 2 answer: {ans}")
