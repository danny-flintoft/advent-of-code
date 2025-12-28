dir_ = "2022/day_09/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data
       
data

head = tail = (0,0)

visited = set([tail])

directions = {
    'R' : (0,1),
    'L' : (0,-1),
    'U' : (-1,0),
    'D' : (1,0)
    }

def move_head(head, d):
   return (head[0]+d[0], head[1]+d[1])

def move_tail(head, tail): 
    if abs(head[0] - tail[0]) > 1:
        x = (head[0]+tail[0])//2
    else:
        x = tail[0]
        
    if abs(head[1] - tail[1]) > 1:
        y = (head[1]+tail[1])//2
    else:
        y = tail[1]
    
    if x != tail[0] and y == tail[1]:
        return(x, head[1])
    elif x == tail[0] and y != tail[1]:
        return(head[0], y)
    else:
        return (x,y)

for row in data:
    d, amt = row.split(' ')
    for _ in range(int(amt)):
        head = move_head(head, directions[d])
        tail = move_tail(head, tail)
        visited.add(tail)

ans = len(visited)
print(f"part 1 answer: {ans}")

######################### part 2 #########################

knots = [(0,0)]*10
visited = set([(0,0)])

for row in data:
    d, amt = row.split(' ')
    for _ in range(int(amt)):
        knots[0] = move_head(knots[0], directions[d])
        
        for i in range(1,len(knots)):
            knots[i] = move_tail(knots[i-1], knots[i])
        visited.add(knots[-1])

ans = len(visited)       
print(f"part 2 answer: {ans}")
