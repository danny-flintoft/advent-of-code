dir_ = "2022/day_06/"
input_data = open(dir_+'input_1.txt', 'r').read()#.split('\n')
test_data = open(dir_+'test_input.txt', 'r').read()#.split('\n')

######################### part 1 #########################
data = input_data

i=0
x = 4
for i in range(len(data)):
    sample = [j for j in data[i:i+x]]
    if len(set(sample)) == x:
        ans = i+x
        break

print(f"part 1 answer: {ans}")

######################### part 2 #########################

i=0
x = 14
for i in range(len(data)):
    sample = [j for j in data[i:i+x]]
    if len(set(sample)) == x:
        ans = i+x
        break
    
print(f"part 2 answer: {ans}")
