dir_ = "2025/day_01/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input_2.txt', 'r').read().split('\n')

######################### part 1 #########################
data = test_data


rotations = [int(x[1:]) if 'R' in x else -int(x[1:]) for x in data]

s = 50
ans = 0
for r in rotations:
    s += r
    s = s%100
    if s == 0:
        ans += 1

print(f"part 1 answer: {ans}")

######################### part 2 #########################


s = 50
ans = 0
for r in rotations:
    if r + s <= 0 and s != 0: # if the values passes positive to negative
        ans += 1
    s += r
    ans += abs(s) // 100 # else increment based on 00's
    s = s%100 # and reset s to the remained 


print(f"part 2 answer: {ans}")