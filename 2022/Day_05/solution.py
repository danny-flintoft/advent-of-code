dir_ = "2022/day_05/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

import re
######################### part 1 #########################
data = input_data

raw_crates = []
moves = []
section = 0
for row in data:
    if row[:2] == ' 1':
        section = 1
    elif section == 0:
        raw_crates.append(row)
    elif section == 1:
        moves.append(row)

pivoted_crates = [list(i) for i in zip(*raw_crates)]

crates = []
for row in pivoted_crates:
    stack = [i for i in row if i not in (' ','[',']')]
    stack.reverse()
    if len(stack) > 0:
        crates.append(stack)

for move in moves[1:]:
    amt, fr, to = [int(i) for i in re.findall('[0-9]+',move)]
    for _ in range(amt):
        val = crates[fr-1].pop()
        crates[to-1].append(val)           

ans = ''.join([c[-1] for c in crates])

print(f"part 1 answer: {ans}")

######################### part 2 #########################

crates = []
for row in pivoted_crates:
    stack = [i for i in row if i not in (' ','[',']')]
    stack.reverse()
    if len(stack) > 0:
        crates.append(stack)
        
for move in moves[1:]:
    amt, fr, to = [int(i) for i in re.findall('[0-9]+',move)]
    to_move = crates[fr-1][-amt:]  
    crates[fr-1] = crates[fr-1][:-amt] 
    crates[to-1] = crates[to-1] + to_move      

ans = ''.join([c[-1] for c in crates])
print(f"part 2 answer: {ans}")
