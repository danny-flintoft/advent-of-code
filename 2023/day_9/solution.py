input_data = open('day_9/input_1.txt', 'r').read().split('\n')
test_data = open('day_9/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data
data = [list(map(int,d.split())) for d in data]

def predict_value(a):
    sum_list = [a[-1]] ## append last value in list to the sum_list
    check = False
    while check != True:
        a = [a[i]-a[i-1] for i in range(1,len(a))] ## get intervals of current lust
        if a[-1] == 0: ## break loop when we hit 0
            break
        sum_list.append(a[-1]) ## append final value of list to sum_list
    return sum(sum_list)

ans = sum(predict_value(a) for a in data)
print("part 1 answer: ", ans)

######################### part 2 #########################
data = input_data
data = [list(map(int,d.split())) for d in data]

def predict_value(a):
    sum_list = [a[0]] ## append first value in list to the sum_list
    check = False
    while check != True:
        a = [a[i]-a[i-1] for i in range(1,len(a))] ## get intervals of current lust
        if a[-1] == 0: ## break loop when we hit 0
            break
        sum_list.append(a[0]) ## append first value of list to sum_list
    sum_list.reverse() ## reverse the list
    x = sum_list[0] ## subtract them sequencially, backwards.
    for i in range(1,len(sum_list)):
        x = sum_list[i] - x        
    return x

ans = sum(predict_value(a) for a in data)
print("part 2 answer: ", ans)
