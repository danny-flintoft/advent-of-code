dir_ = "2025/day_06/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

from math import prod

######################### part 1 #########################
data = input_data

lists = []
for line in data:
    items = [x for x  in line.split(' ') if x != '']
    lists.append(items)
 
equations = []
for i in range(len(lists[0])):
    equation = []
    for j in range(len(lists)):
        equation.append(lists[j][i])
    equations.append(equation)

ans = 0
for equation in equations:
    if equation[-1] == '+':
        ans += sum(int(x) for x in equation[:-1])
    else:
        ans += prod(int(x) for x in equation[:-1])        

print(f"part 1 answer: {ans}")

######################### part 2 #########################

operators = data[-1]

equations = []
equation = []
for i, o in enumerate(operators):
    if o in ('*','+'):
        if equation != []:
            equations.append(equation) ## log last equation (ignoring the starter blank equation)
        equation = [o] ## and start a new one
     
    number = []
    for line in data[:-1]:
        number.append(line[i])
        
    number = ''.join(number)
    if number.strip() != '': # if it's not completely blank
        equation.append(int(number))
equations.append(equation) ## append last equation 

ans = 0
for equation in equations:
    if equation[0] == '+':
        ans += sum(int(x) for x in equation[1:])
    else:
        ans += prod(int(x) for x in equation[1:])

print(f"part 2 answer: {ans}")
