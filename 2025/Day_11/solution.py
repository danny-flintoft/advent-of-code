dir_ = "2025/day_11/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
test_data_2 = open(dir_+'test_input_2.txt', 'r').read().split('\n')

from collections import deque

######################### part 1 #########################

data = input_data

grid = dict()
for d in data:
    parts = d.split(' ')
    
    if parts[0] == 'you:':
        queue = deque(parts[1:]) 
    grid[parts[0][:-1]] = (parts[1:], 0)

while queue:
    device = queue.popleft()
    grid[device] = (grid[device][0], grid[device][1]+1)
    for d in grid[device][0]:  
        if d != 'out':
            queue.append(d)

ans = 0
for item in grid.values():
    if 'out' in item[0]:
        ans += item[1]
 
print(f"part 1 answer: {ans}")

######################### part 2 #########################

data = input_data

# extra values track if we have hit fft and dac --> (device, 0, 0)
# this doesn't work yet! only part 1 works! 

grid = dict()
for d in data:
    parts = d.split(' ')
    
    if parts[0] == 'svr:':
        queue = deque((p, 0, 0) for p in parts[1:])
    grid[parts[0][:-1]] = (parts[1:], 0)
    
i=1
while queue:
    print(i)
    i+=1
    device = queue.popleft()
    if device[0] == 'fft':
        fft = 1
        dac = device[2]
    elif device[0] == 'dac':
        dac = 1
        fft = device[1]
        print('dac')
    else:
        fft = device[1]
        dac = device[2]
    
    if fft == 1 and dac == 1:
        grid[device[0]] = (grid[device[0]][0], grid[device[0]][1]+1)
    for d in grid[device[0]][0]:
        if d != 'out':
            queue.append((d, fft, dac))    
    
ans = 0
for item in grid.values():
    if 'out' in item[0]:
        ans += item[1]

print(f"part 2 answer: {ans}")


