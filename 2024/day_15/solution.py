dir_ = "2024/day_15/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n\n')
data = input_data

## this is painfully unreadable, espescially part 2! best not to try!
######################### part 1 #########################
## p = position

## get grid and movements
grid_ = data[0].split('\n')
movements = data[-1].replace('\n','')

rows = len(grid_)
cols = len(grid_[0])
grid = {}
for x in range(cols):
    for y in range(rows):
        value = grid_[y][x]
        grid[(x,y)] = value
        if value == '@':
            p = (x,y)          
               
## define movements
movement_dict = {'>':(1,0),
                 '<':(-1,0),
                 '^':(0,-1),
                 'v':(0,1)}   

def scan():
    scan_positions = []
    scan_values = []
    for i in range(1,max(cols-p[0],rows-p[1],cols)):
        scan_position = (p[0]+m[0]*i,p[1]+m[1]*i)
        scan_value = grid[scan_position]
        scan_positions.append(scan_position)
        scan_values.append(scan_value)
        if scan_value == '#':
            break
    return scan_positions, scan_values    

def plot_grid(grid,on=True):
    if on:
        plot = []
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(grid[(x,y)])
            plot.append(row)        
        for row in plot:
            print(''.join(row))
    
for m_ in movements:
    m = movement_dict[m_]   
    scan_positions, scan_values = scan()
    if scan_values[0] == '.': ## if first position is a gap, move into it
        grid[p] = '.'
        p = (p[0]+m[0],p[1]+m[1])
        grid[p] = '@'
    elif scan_values[0] == '#': ## if first position is a wall, do nothing
        pass
    elif scan_values[0] == 'O': ## if first position is a box
        for i in range(len(scan_values)):
            if scan_values[i] == '.': ## keep looking for a space
                grid[scan_positions[i]] = 'O' ## push all the boxes
                grid[p] = '.'
                p = scan_positions[0]
                grid[p] = '@'
                break 
    plot_grid(grid,False)

ans = 0
for key, value in grid.items():
    if value == 'O':
        gps = (key[1]*100)+key[0]
        ans += gps

print("part 1 answer:", ans)

######################### part 2 #########################

## get grid and movements
grid_ = data[0].split('\n')
expanded_grid = []
for row in grid_:
    expanded_row = (row.replace("#","##")
                    .replace("O","[]")
                    .replace(".","..")
                    .replace("@","@."))
    expanded_grid.append(expanded_row)

rows = len(expanded_grid)
cols = len(expanded_grid[0])
grid = {}
for x in range(cols):
    for y in range(rows):
        value = expanded_grid[y][x]
        grid[(x,y)] = value
        if value == '@':
            p = (x,y)

## make the movements             
plot_grid(grid,False)

for iter_,m_ in enumerate(movements):  
    #input()     
    m = movement_dict[m_]
    new_p = (p[0]+m[0],p[1]+m[1])         
    new_val = grid[new_p]  
  
    if new_val == '.': ## if space, move
        grid[p] = '.'
        p = new_p ## move p
        grid[p] = '@'  
            
    elif new_val == '#': ## if wall, do nothing
        pass   
               
    elif new_val in ['[',']'] and m_ in ['<','>']: ## if wall <>, move
        i=1
        while True:
            next_p = (p[0]+m[0]*i,p[1]+m[1]*i)  
            next_val = grid[next_p]
            if next_val == '#':
                break
            elif next_val in ['[',']']:
                i+=1
                pass
            elif next_val == '.':
                ## this block of code moves a series of boxed horizontally
                for j in reversed(range(1,i+1)):
                    p_ = (p[0]+m[0]*j,p[1]+m[1]*j)
                    p_mod = (p[0]+m[0]*(j-1),p[1]+m[1]*(j-1))
                    v_ = grid[p_] 
                    v_mod = grid[p_mod] 
                    grid[p_] = v_mod     
                grid[p] = '.' ## add gap from moved boxes
                p = new_p ## move p
                grid[p] = '@'
                break       
            
    elif new_val in ['[',']'] and m_ in ['^','v']: ## if wall ^v, move
        box_positions = [new_p]
        if new_val == '[':
            box_positions.append((new_p[0]+1,new_p[1]))
        else:
            box_positions.append((new_p[0]-1,new_p[1]))
        layer_1_boxes = box_positions.copy()
        ## for each box position, check what is above it
        checked_box_positions = []
        wall = False
        while True:
            next_layer = []
            for box_position in box_positions:
                if box_position not in checked_box_positions:
                    checked_box_positions.append(box_position)
                    p_ = (box_position[0]+m[0],box_position[1]+m[1])
                    v_ = grid[p_]
                    if v_ == '.':
                        pass
                    if v_ == '#':
                        wall = True                        
                        break
                    if v_ == '[':
                        next_layer.append(p_)
                        next_layer.append((p_[0]+1,p_[1]))
                    if v_ == ']':
                        next_layer.append(p_)
                        next_layer.append((p_[0]-1,p_[1]))
            if wall:
                break
            box_positions = box_positions + next_layer
            if wall:## if there was a wall we do nothing
                continue
            elif len(next_layer)==0: ## if there is space to move, move
                done = []
                for box_position in box_positions[::-1]:
                    if box_position not in done:
                        done.append(box_position)
                        ## next position above becomes current value
                        p_ = (box_position[0]+m[0],box_position[1]+m[1])
                        grid[p_] = grid[box_position]
                        grid[box_position] = '.'
                        if box_position in layer_1_boxes:
                            grid[box_position] = '.' 
                grid[p] = '.' ## add gap from moved boxes
                p = new_p ## move p
                grid[p] = '@'                
                break
            else: ## if there were boxes and no walls, check next layer!
                 pass   
    
    plot_grid(grid,False)
          
ans = 0
for key, value in grid.items():
    if value == '[':
        gps = (key[1]*100)+key[0]
        ans += gps
        
print("part 2 answer:", ans)