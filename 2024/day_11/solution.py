dir_ = "2024/day_11/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

######################### part 1 & 2 #########################

stones = data[0].split(' ')

def add_to_counter(counter, stone, amount=1):
    if stone in counter.keys():
        counter[stone] += amount
    else:
        counter[stone] = amount
    
counter = {}    
for stone in stones:
    add_to_counter(counter, stone)

def blink(stone):
    length = len(stone)
    if stone == '0':
        output = ['1']
    elif length%2 == 0:
        output = [stone[:int(length/2)],stone[int(length/2):]]
    else:
        output = [(str(int(stone)*2024))]
    return output

for i in range(75):
    counter_ = {}     
    for key,val in counter.items():
        output = blink(key)
        for stone in output:            
            add_to_counter(counter_,str(int(stone)),val)            
    counter = counter_.copy()
    if i == 24:
        p1 = sum(counter.values())
    if i == 74:
        p2 = sum(counter.values())

print("part 1 answer:", p1)
print("part 2 answer:", p2)
