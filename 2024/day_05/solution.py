dir_ = "2024/day_05/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n\n')
data = input_data

rules = data[0].split('\n')
updates = [x.split(',') for x in data[1].split('\n')]
updates = [[int(x) for x in y] for y in updates] ## cast as ints
    
######################### part 1 #########################

passes = []
for update in updates:
    pass_ = True
    for rule in rules:    
        a = int(rule.split('|')[0])
        b = int(rule.split('|')[1]) 
        try:
            a_index = update.index(a)
            b_index = update.index(b)
            if a_index > b_index:
                pass_ = False
        except:
            pass
    if pass_ == True:
        passes.append(update)

ans = 0
for p in passes:
    mid_num = p[int((len(p)-1)/2)]
    ans += mid_num

print("part 1 answer:", ans)

######################### part 2 #########################

## get all failed lists
fails = [u for u in updates if u not in passes]  

## define function to order each update correctly
def order_update(update):
    update_ordered = []
    for u in update:
        
        ## for every list position, cycle through until no rules are violated
        for i in range(len(update_ordered)+1):
            broken = False
            update_variant = update_ordered.copy()
            update_variant.insert(i,u)
            
            ## check if rules are violated
            for rule in [r for r in rules if str(u) in r]:  
                a = int(rule.split('|')[0])
                b = int(rule.split('|')[1]) 
                try:
                    a_index = update_variant.index(a)
                    b_index = update_variant.index(b)
                    if a_index > b_index:
                        broken = True
                except:
                    pass
            ## if none of the rules are violated, update order & end loop  
            if broken == False:
                update_ordered = update_variant.copy()
                break ## break the loop
                
    return update_ordered

passes = []
for update in fails:
    update_ordered = order_update(update)
    passes.append(update_ordered)

ans = 0
for p in passes:
    mid_num = p[int((len(p)-1)/2)]
    ans += mid_num

print("part 2 answer:", ans)