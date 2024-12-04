dir_ = "2024/day_03/"
input_data = open(dir_+'input_1.txt', 'r').read()#.split('\n')
test_data = open(dir_+'test_input.txt', 'r').read()#.split('\n')
test_data_2 = open(dir_+'test_input_2.txt', 'r').read()#.split('\n')
data = input_data

import re    
######################### part 1 #########################

## find all matching text
regex = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"
matches = re.findall(regex,data)

## cycle through each - get prod of numbers and sum
ans = 0
for match_ in matches:
    numbers = [int(x) for x in re.findall('[0-9]+',match_)]
    prod = 1
    for number in numbers:
        prod = prod * number
    ans += prod

print("part 1 answer:", ans)

######################### part 2 #########################

## find all matching text
regex = "do\\(\\)|don't\\(\\)|mul\\([0-9]{1,3},[0-9]{1,3}\\)"
matches = re.findall(regex,data)

## cycle through each - get prod of numbers and sum
## use mul variable to 0 prods when don't is in action
mul = 1
ans = 0
for match_ in matches:
    if "don't" in match_:
        mul = 0
    elif 'do' in match_:
        mul = 1
    else:
        numbers = [int(x) for x in re.findall('[0-9]+',match_)]
        prod = mul
        for number in numbers:
            prod = prod * number
        ans += prod

print("part 2 answer:", ans)