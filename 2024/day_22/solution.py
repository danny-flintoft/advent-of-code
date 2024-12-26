dir_ = "2024/day_22/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

from math import floor
from collections import defaultdict

######################### part 1 #########################

SNs = [int(x) for x in data]

cache = {}
def evolve(SN):        
    if SN in cache:
        return cache[SN]
    else:
        SN_ = ((SN*64)^SN)%16777216
        SN_ = (floor(SN_/32)^SN_)%16777216
        SN_ = ((SN_*2048)^SN_)%16777216
        old_price = SN%10
        new_price = SN_%10
        change = new_price-old_price
        cache[SN] = (SN_, new_price, change)
        return SN_, new_price, change

ans = 0
for SN in SNs:
    for i in range(2000):
        SN,_,_ = evolve(SN)
    ans += SN

print("part 1 answer:", ans)      

######################### part 2 #########################

scores = defaultdict(int)
for SN in SNs:
    seen = set()
    pattern = []
    for i in range(2000):
        SN, price, change = evolve(SN)
        pattern.append(change)
        if len(pattern) == 4:
            if not tuple(pattern) in seen:
                scores[tuple(pattern)] += price
                seen.add(tuple(pattern))
            pattern.pop(0)
 
ans = max(scores.values())
print("part 2 answer:", ans)   
