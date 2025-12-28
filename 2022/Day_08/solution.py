dir_ = "2022/day_08/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

X = len(data[0])
Y = len(data)

visible = []

# from the top
    
for x in range(X):
    last = -1
    for y in range(Y):
        height = int(data[y][x])
        if height > last:
            visible.append((x,y))
            last = height

# from the bottom
    
for x in range(X):
    last = -1
    for y in reversed(range(Y)):
        height = int(data[y][x])
        if height > last:
            visible.append((x,y))
            last = height

# from the left

for y in range(Y):
    last = -1
    for x in range(X):
        height = int(data[y][x])
        if height > last:
            visible.append((x,y))
            last = height
 
# from the right

for y in range(Y):
    last = -1
    for x in reversed(range(X)):
        height = int(data[y][x])
        if height > last:
            visible.append((x,y))
            last = height
            
ans = len(set(visible))
print(f"part 1 answer: {ans}")

######################### part 2 #########################

ans = 0
for x in range(X):
    for y in range(Y):
        cell = (x,y)
        height = int(data[y][x])
        
        # check up 
        score_u = 0
        for y_ in reversed(range(y)):
            height_ = int(data[y_][x])
            score_u += 1
            if height_ >= height:
                break
            
        # check down
        score_d = 0
        for y_ in range(y+1,Y):
            height_ = int(data[y_][x])
            score_d += 1
            if height_ >= height:
                break
            
        # check left 
        score_l = 0
        for x_ in reversed(range(x)):
            height_ = int(data[y][x_])
            score_l += 1
            if height_ >= height:
                break
            
        # check right 
        score_r = 0
        for x_ in range(x+1,X):
            height_ = int(data[y][x_])
            score_r += 1
            if height_ >= height:
                break
        
        score = score_u * score_d * score_l * score_r
        ans = max(ans, score)
        
print(f"part 2 answer: {ans}")