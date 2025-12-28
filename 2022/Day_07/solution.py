dir_ = "2022/day_07/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

ans = 0
dir_sizes = []
for j, d in enumerate(data):    
    
    if d[:4] == '$ cd' and d != '$ cd ..':
        dir_size = 0
        i = j+1
        depth = 1
        
        while depth > 0 and i < len(data):
            row = data[i] 
            if row[:3] == 'dir':
                pass
            elif row == '$ cd ..':
                depth -= 1
            elif row[:4] == '$ cd':
                depth += 1
            elif row[0] != '$':
                dir_size += int(row.split(' ')[0])
            i += 1

        dir_sizes.append(dir_size)
        if dir_size <= 100000:
            ans += dir_size          

print(f"part 1 answer: {ans}")

######################### part 2 #########################

dir_sizes.sort()
size = 30000000 - (70000000 - dir_sizes[-1])

ans = min(d for d in dir_sizes if d >= size)
print(f"part 2 answer: {ans}")