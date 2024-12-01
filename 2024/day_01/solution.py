dir_ = "2024/day_01/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

## generate empty lists
l_1, l_2 = [], []

## populate lists with data values
for l in data:
    locations = l.split("   ")
    l_1.append(int(locations[0]))
    l_2.append(int(locations[1]))

## sort lists    
l_1.sort()
l_2.sort()

## compare lists
ans = sum([abs(a-b) for a,b in zip(l_1,l_2)])
print("part 1 answer:", ans)

######################### part 2 #########################

ans = sum([x*l_2.count(x) for x in l_1])
    
print("part 2 answer:", ans)