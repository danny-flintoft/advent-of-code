dir_ = "2025/day_11/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
test_data_2 = open(dir_+'test_input_2.txt', 'r').read().split('\n')

from functools import cache

######################### part 1 #########################

data = input_data

# build grid
grid = dict()
for d in data:
    key, value = d.split(': ')  
    grid[key] = value.split(' ')

# recursive function to count paths
@cache
def count_paths(source, destination):
    if source == destination: 
        return 1
    else:
        return sum(count_paths(s, destination) for s in grid.get(source,[]))

ans = count_paths('you','out')
 
print(f"part 1 answer: {ans}")

######################### part 2 #########################

a1 = count_paths('svr','fft') * count_paths('fft','dac') * count_paths('dac','out')
a2 = count_paths('svr','dac') * count_paths('dac','fft') * count_paths('fft','out')
ans = a1 + a2

print(f"part 2 answer: {ans}")


