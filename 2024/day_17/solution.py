dir_ = "2024/day_17/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

from math import trunc
######################### part 1 #########################

def setup_program(data):
    A = int(data[0].split(": ")[1])
    B = int(data[1].split(": ")[1])
    C = int(data[2].split(": ")[1])
    program = [int(x) for x in data[4].split(": ")[1].split(',')]  
    pointer = 0    
    return A,B,C,program,pointer

def get_combo_operand(A,B,C,operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C

def run_program(A,B,C,program,pointer):
    output = []   
    while True:
        if pointer >= len(program):
            break
        else:
            opcode = program[pointer]
            operand = program[pointer+1]
           
        if opcode == 0:
            A = trunc(A/(2**get_combo_operand(A,B,C,operand)))
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = get_combo_operand(A,B,C,operand)%8
        elif opcode == 3:
            if A != 0:
                pointer = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output.append(get_combo_operand(A,B,C,operand)%8)
        elif opcode == 6:
            B = trunc(A/(2**get_combo_operand(A,B,C,operand)))
        elif opcode == 7:
            C = trunc(A/(2**get_combo_operand(A,B,C,operand)))
        pointer += 2
    return output    

A,B,C,program,pointer = setup_program(data)
output = run_program(A,B,C,program,pointer)

ans = ','.join((str(x) for x in output))
print("part 1 answer:", ans)

8*64*512
######################### part 2 #########################

# A,B,C,program,pointer = setup_program(data)

# i=5
# A = 0
# good_a = []
# for A in range(10000000):
#     output = run_program(A,B,C,program,pointer)
#     if len(output) > i:
#         if output[i] == program[i]:
#             good_a.append(A)
                    
# count = 1
# for i in range(len(good_a)-1):
#     if good_a[i+1] - good_a[i] == 1:
#         count+=1
#     else:
#         break

# diff = 0
# for i in range(len(good_a)-1):
#     diff_ = good_a[i+1] - good_a[i]
#     if diff_ != 1:
#         diff = diff_

# print(count)
# print(diff)
# print(min(good_a))


# def get_vals(mod,inc,start):
#     vals = []
#     x=start
#     for i in range(1,1000000):
#         vals.append(x)
#         if i%mod==0:
#             x+=inc
#         else:
#             x+=1
#     return vals

# vals_0 = get_vals(8,57,0)
# vals_1 = get_vals(64,449,192)
# vals_2 = get_vals(512,3585,2560)
# vals_3 = get_vals(4096,28673,16384)
# vals_4 = get_vals(32768,229377,98304)
# vals_5 = get_vals(229376,1835009,32768)

# vals_5[:600]
# good_a[:600]

# common = set(vals_0) & set(vals_1) & set(vals_2) & set(vals_3) & set(vals_4) & set(vals_5)
# min(common)

print("part 2 answer:", ans)