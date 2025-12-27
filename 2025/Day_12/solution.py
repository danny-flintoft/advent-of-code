dir_ = "2025/day_12/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################

data = input_data
regions = [row for row in data if len(row) > 5]

ans = 0
for region in regions:
    area, units_list = region.split(': ')
    units = sum(int(x) for x in units_list.split(' '))
    X, Y = area.split('x')
    if int(X)//3 * int(Y)//3 >= units:
        ans += 1
    
print(f"part 1 answer: {ans}")



