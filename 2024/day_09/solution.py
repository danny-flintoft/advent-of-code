dir_ = "2024/day_09/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

######################### part 1 #########################

d = data[0]

blocks = []
id_ = 0
for i,val in enumerate(d):
    if i%2 == 0:        
        for x in range(int(val)):
            blocks.append(str(id_))
        id_+=1            
    else:
        for x in range(int(val)):
            blocks.append('.')

for i in range(len(blocks)):
    if i == len(blocks):
        break
    if blocks[i] == '.':
        done = False
        while done == False:
            val = blocks.pop()
            if val != '.':
                blocks[i] = val
                done = True
    
ans = 0
for i,n in enumerate(blocks):
    ans += int(n)*i
        
print("part 1 answer:", ans)


######################### part 2 #########################

## order our input as tuple - value (0/1/2/3/. etc) and number of occurences
order = []
val = 0
for i,x in enumerate(d):
    if i%2 == 0:
        order.append((int(x),val))
        val+=1
    else:
        order.append((int(x),'.'))
        
## starting at the back of our set, try to move each file into a space 
## of '.'s further forwards in the order
for i in range(1,len(order)):
    file = order[-i]    
    if file[1] != '.':
        j=0
        while True:
            space = order[j]
            if space[1] == '.' and space[0] >= file[0]:
                order.insert(j,file) ## insert file
                j+=1
                order[j] = (order[j][0]-order[-i][0],order[j][1]) ## reduce dots
                order[-i] = (order[-i][0],'.') ## change original file pos to dots
                break
            else:
                j+=1
                if j > len(order)-i:
                    break

## turn order into a list for counting
blocks = []
for file in order:
    if file[0]!=0:
        for i in range(file[0]):
            blocks.append(str(file[1]))

##count
ans = 0
for i,n in enumerate(blocks):
    if n != '.':
        ans += int(n)*i

print("part 2 answer:", ans)