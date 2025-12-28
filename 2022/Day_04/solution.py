dir_ = "2022/day_04/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

ans = 0
for d in data:
    
    a,b = [[int(j) for j in i.split('-')] for i in d.split(',')]
    
    if a[0] <= b[0] and a[1] >= b[1]:
        ans += 1
    elif b[0] <= a[0] and b[1] >= a[1]:
        ans += 1

print(f"part 1 answer: {ans}")

######################### part 2 #########################

ans = 0
for d in data:
    
    a,b = [[int(j) for j in i.split('-')] for i in d.split(',')]
    
    if a[0] <= b[0] and a[1] >= b[0]:
        ans += 1
    elif a[1] >= b[1] and a[0] <= b[1]:
        ans += 1
    elif b[0] <= a[0] and b[1] >= a[0]:
        ans += 1
    elif b[1] >= a[1] and b[0] <= a[1]:
        ans += 1

print(f"part 2 answer: {ans}")