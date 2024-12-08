dir_ = "2024/day_07/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = test_data
  
from itertools import permutations 
######################### part 1 #########################

## define function to get components of equation
def get_parts(row):
    output, inputs = row.split(": ")
    output = int(output)
    inputs = [int(x) for x in inputs.split(" ")]
    return output, inputs

## define function to evaluate equation
def evaluate(inputs,operators):
    evaluation = inputs[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            evaluation += inputs[i+1]   
        else:
            evaluation *= inputs[i+1]
    return evaluation


ans = 0
for row in data:
    output, inputs = get_parts(row)
    print(f"\n\n>{output}: {inputs}\n")
    
    ## broken check
    x=1
    for y in inputs:
        x*=y
    if x < output and 1 not in inputs:
        continue
    
    for mul in range(len(inputs)):
        # print("mul:",mul)
        operators = mul*'*'+(len(inputs)-1-mul)*'+'                                 
        list_of_operators = set(permutations (operators,len(operators)))
        
        evals = set()
        for operators in list_of_operators:
            evaluation = evaluate(inputs,operators)
            evals.add(evaluation)
        # print(evals, output)
        if output in evals:
            print("possible")
            ans += output
            break
        elif min(evals)>output:
            print("impossible")
            break
        else:
            pass


print("part 1 answer:", ans)
######################### part 2 #########################

# print("part 2 answer:", ans)

# ans = 0
# for row in data:
    
#     output, inputs = get_parts(row)
#     print(f"\n\n>{output}: {inputs}\n")
#     operators = ['+' for i in range(len(inputs)-1)]
#     list_of_operators = [operators]
    
#     while True:
#         evals = []
#         for operators in list_of_operators:
#             evaluation = evaluate(inputs,operators)
#             evals.append(evaluation)
#         print(evals, output)
#         if output in evals:
#             print("possible")
#             ans += output
#             break
#         elif min(evals)>output:
#             print("impossible")
#             break
#         else:
#             ## take the operators with the lowest evaluation as our base, and modify
#             operators = list_of_operators[np.argmin(evals)] 
#             print("new base is",operators)  
#             if sum(1 for o in operators if o == '+') == 0:
#                 break
#             list_of_operators = []
#             for i in range(len(operators)):
#                 if operators[i] != '*':
#                     mod = operators.copy()
#                     mod = mod[:i] + ['*'] + mod[i+1:]
#                     list_of_operators.append(mod)

# print("part 1 answer:", ans)





