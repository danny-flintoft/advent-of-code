dir_ = "2025/day_07/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')


######################### part 1 #########################
data = input_data


# track the 'power' of a beam, e.g. if two beams land on the same cell their
# power is combined.

X = len(data[0])
Y = len(data)

p1_ans = 0

# engage trachyon beam

grid = dict()
for y in range(Y):
    for x in range(X):
        
        if (x,y) not in grid.keys():
            grid[(x,y)] = (data[y][x],0)
    
        if y > 0:
            if grid[(x,y-1)][0] == 'S':
                grid[(x,y)] = ('|',1)
            
            if grid[(x,y-1)][0] == '|' and grid[(x,y)][0] == '|':
                new_power = grid[(x,y-1)][1] + grid[(x,y)][1]
                grid[(x,y)] = ('|', new_power)
                    
            if grid[(x,y-1)][0] == '|' and grid[(x,y)][0] == '.':
                grid[(x,y)] = grid[(x,y-1)]                      
                
            if grid[(x,y-1)][0] == '|' and grid[(x,y)][0] == '^':
                
                p1_ans += 1
                
                if grid[(x-1,y)][0] == '|':
                    new_power = grid[(x-1,y)][1] + grid[(x,y-1)][1]
                    grid[(x-1,y)] = ('|', new_power)
                else:
                    grid[(x-1,y)] = ('|', grid[(x,y-1)][1])
                    
                grid[(x+1,y)] = ('|', grid[(x,y-1)][1])
            
# print the grid
for y in range(Y):
    line = []
    for x in range(X):
        if grid[(x,y)][0] == '^':
            line.append('^')
        else:
            line.append(grid[(x,y)][0])
    print(line)

p2_ans = sum(v[1] for k, v in grid.items() if k[1] == Y-1)

print(f"part 1 answer: {p1_ans}")
print(f"part 2 answer: {p2_ans}")
