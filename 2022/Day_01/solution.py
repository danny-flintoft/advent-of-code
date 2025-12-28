dir_ = "2022/day_01/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n\n')

######################### part 1 #########################
data = input_data

items = [[int(j) for j in i.split('\n')] for i in data]
calories = [sum(i) for i in items]
calories.sort()

ans = calories[-1]
print(f"part 1 answer: {ans}")

######################### part 2 #########################

ans = sum(calories[-3:])
print(f"part 2 answer: {ans}")