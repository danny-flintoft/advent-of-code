dir_ = "2024/day_19/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n\n')
data = test_data

######################### part 1 & 2 #########################

## set inputs and outputs
inputs = data[0].split(", ")
outputs = data[1].split('\n')

results = {}
def make_towel(inputs,output):
    if output in results:
        return results[output]
    result = 0
    if not output:
        result = 1
    for input_ in inputs:
        if output.startswith(input_):
            result += make_towel(inputs,output[len(input_):])
    results[output] = result
    return result

p1_ans = 0
p2_ans = 0
for output in outputs:
    result = make_towel(inputs,output)
    if result > 0:
        p1_ans += 1
    p2_ans += result

print("part 1 answer:", p1_ans) 
print("part 2 answer:", p2_ans)      