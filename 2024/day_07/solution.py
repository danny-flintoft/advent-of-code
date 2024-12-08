dir_ = "2024/day_07/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data
  
######################### part 1 #########################

## define function to get components of equation
def get_parts(row):
    output, inputs = row.split(": ")
    output = int(output)
    inputs = [int(x) for x in inputs.split(" ")]
    return output, inputs

## using recursion - check if we ever reach a true state by adding
## or multiplying the first 2 numbers in the list
def is_valid(output, inputs):
    if len(inputs) == 1:
        return inputs[0] == output
    if is_valid(output,[inputs[0]+inputs[1]] + inputs[2:]):
        return True
    if is_valid(output,[inputs[0]*inputs[1]] + inputs[2:]):
        return True

ans = 0   
for row in data:
    output, inputs = get_parts(row)  
    if is_valid(output,inputs):
        ans += output

print("part 1 answer:", ans)
######################### part 2 #########################

## modify function to include the option of concatenating the first 2 numbers
def is_valid(output, inputs):
    if len(inputs) == 1:
        return inputs[0] == output
    if is_valid(output,[inputs[0]+inputs[1]] + inputs[2:]):
        return True
    if is_valid(output,[inputs[0]*inputs[1]] + inputs[2:]):
        return True
    if is_valid(output, [int(str(inputs[0])+str(inputs[1]))] + inputs[2:]):
        return True

ans = 0   
for row in data:
    output, inputs = get_parts(row)  
    if is_valid(output,inputs):
        ans += output

print("part 2 answer:", ans)
