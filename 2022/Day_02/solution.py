dir_ = "2022/day_02/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

scores = {
    'X':1,
    'Y':2,
    'Z':3
    }

wins = ['A Y', 'B Z', 'C X']
draws = ['A X', 'B Y', 'C Z']

def evaluate_moves(data):
    ans = 0
    for d in data:
        ans += scores[d[-1]]
        if d in wins:
            ans += 6
        elif d in draws:
            ans += 3
    return ans

ans = evaluate_moves(data)

print(f"part 1 answer: {ans}")

######################### part 2 #########################

moves = {
    'A': ('X','Y','Z'),
    'B': ('Y','Z','X'),
    'C': ('Z','X','Y')
    }

ans = 0
for d in data:
    if d[-1] == 'X':
        choice = moves[d[0]][2]
        ans += scores[choice]
    elif d[-1] == 'Y':
        choice = moves[d[0]][0]
        ans += scores[choice]+3
    elif d[-1] == 'Z':
        choice = moves[d[0]][1]
        ans += scores[choice]+6

print(f"part 2 answer: {ans}")