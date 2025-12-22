dir_ = "2025/day_10/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

from itertools import combinations_with_replacement

######################### part 1 #########################
data = input_data

# get lights data
lights = [d.split(' ', 1)[0] for d in data]
lights = [tuple(1 if l == '#' else 0 for l in light[1:-1]) for light in lights]

# get buttons data
buttons = []
for d in data:
    buttons_ = []
    for string in d.split(' ')[1:-1]:
        string = tuple(int(i) for i in string.replace('(','').replace(')','').split(','))
        buttons_.append(string)
    buttons.append(buttons_)

# define function for pressing a series of buttons
def press_buttons(light, button_set):
    length = len(light)
    indexes = dict.fromkeys(list(range(length)), 0)
    for button in button_set:
        for b in button:
            if b < length:
                indexes[b] += 1
    return tuple(i%2 for i in indexes.values())

# cycle through all combinations, starting with 1 button, then 2, 3 etc
ans = 0
for light, button_set in zip(lights, buttons):
    
    i = 1 # start with 1 button at iterate
    solved = False
    while solved == False:
        for combo in combinations_with_replacement(button_set, i):
            result = press_buttons(light, combo)
            if result == light:
                solved = True
                ans += i
                break
        i += 1
 
print(f"part 1 answer: {ans}")

######################### part 2 #########################

# part 2 doesn't work yet! too tough!

joltages = [d.split(' ')[-1] for d in data]
joltages = [
    tuple(int(j) for j in joltage.replace('{','').replace('}','').split(','))
    for joltage in joltages]

# re-define function for pressing a series of buttons, this item for joltages
def press_buttons(light, button_set):
    length = len(light)
    indexes = dict.fromkeys(list(range(length)), 0)
    for button in button_set:
        for b in button:
            if b < length:
                indexes[b] += 1
    return tuple(indexes.values())

ans = 0
for joltage, button_set in zip(joltages, buttons):
    
    i = max(joltage) # start with 1 button at iterate
    solved = False
    while solved == False:
        for combo in combinations_with_replacement(button_set, i):
            result = press_buttons(joltage, combo)
            if result == joltage:
                solved = True
                ans += i
                print(i)
                break
        i += 1

print(f"part 2 answer: {ans}")


