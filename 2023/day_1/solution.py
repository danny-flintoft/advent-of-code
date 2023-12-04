input_data = open('day_1/input_1.txt', 'r').read().split('\n')
test_data = open('day_1/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data 

count=0
for a in data:
    numbers = [x for x in a if x.isdigit()]
    count += int(''.join([numbers[0],numbers[-1]]))

print("part 1 answer:", count)

######################### part 2 #########################
import re
data = input_data

num_dict = {
            'one':'1'
            ,'two':'2'
            ,'three':'3'
            ,'four':'4'
            ,'five':'5'
            ,'six':'6'
            ,'seven':'7'
            ,'eight':'8'
            ,'nine':'9'
            ,'1':'1'
            ,'2':'2'
            ,'3':'3'
            ,'4':'4'
            ,'5':'5'
            ,'6':'6'
            ,'7':'7'
            ,'8':'8'
            ,'9':'9'
            }

count=0
for a in data:   
    numbers = re.findall("(?=("+'|'.join(num_dict.keys())+"))",a)
    int_numbers = [num_dict[x] for x in numbers]
    count += int(''.join([int_numbers[0],int_numbers[-1]]))

print("part 2 answer:", count)





    
