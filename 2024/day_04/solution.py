dir_ = "2024/day_04/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
test_data_2 = open(dir_+'test_input_2.txt', 'r').read().split('\n')
data = input_data
  
######################### part 1 #########################

## for each co-ordinate, map text 3 steps in each direction

X = len(data[0])
Y = len(data)
map_ = [0,1,2,3]
masks = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]

ans = 0
for x in range(X):
    for y in range(Y):
        for mask in masks:
            x_map = [mask[0] * i for i in map_]
            y_map = [mask[1] * i for i in map_]    
            locations = [[x+x_, y+y_] for x_,y_ in zip(x_map,y_map)]
            word = []
            for loc in locations:
                letter = ''
                if loc[0] >= 0 and loc[0] < X and loc[1] >= 0 and loc[1] < Y:
                    letter = data[loc[1]][loc[0]]
                word.append(letter)
            word = ''.join(word)                
            if word == 'XMAS':
                ans += 1

print("part 1 answer:", ans)

######################### part 2 #########################

x_map = [1,-1,-1,1]
y_map = [1,-1,1,-1]

ans = 0
for x in range(X):
    for y in range(Y):       
        if data[y][x] == 'A':
            locations = [[x+x_, y+y_] for x_,y_ in zip(x_map,y_map)]
            word = []
            for loc in locations:                
                letter = ''
                if loc[0] >= 0 and loc[0] < X and loc[1] >= 0 and loc[1] < Y:
                    letter = data[loc[1]][loc[0]]
                word.append(letter)
            word = ''.join(word)
            if word in ['SMSM','MSMS','SMMS','MSSM']:
                ans+=1
        
print("part 2 answer:", ans)