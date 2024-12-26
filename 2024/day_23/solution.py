dir_ = "2024/day_23/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

from collections import defaultdict

######################### part 1 #########################

## build dict of all links
links = defaultdict(set)
for row in data:
    pc_1, pc_2 = row.split("-")
    links[pc_1].add(pc_2)
    links[pc_2].add(pc_1)
 
## find groups of 3 linked computers
sets = set()       
for key, values in links.items():
    for v in values:
        for v2 in values:
            if v in links[v2]:
                sets.add(tuple(sorted([key,v,v2])))

## count sets with a computer starting with a t
ans = 0
for set_ in sets:
    if 't' in set_[0][0] or 't' in set_[1][0] or 't' in set_[2][0]:
        ans += 1
print("part 1 answer:", ans)      

######################### part 2 #########################


pcs = list(links.keys())

ans = []
for pc_1 in pcs:
    set_ = set()
    set_.add(pc_1)
    for pc_2 in pcs:
        viable = True
        for pc_3 in set_:
            if not pc_2 in links[pc_3]:
                viable = False
        if viable:
            set_.add(pc_2)
    if len(set_) > len(ans):
        ans = set_

ans = sorted(ans) 
ans = ','.join(ans)
      
print("part 2 answer:", ans)   
