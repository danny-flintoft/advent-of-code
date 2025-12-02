dir_ = "2025/day_02/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

ranges = data[0].split(',')
invalid_ids = 0

# for each range
for range_ in ranges:
    
    from_, to = [int(x) for x in range_.split('-')]
    
    # for each id in the range, check if left half = right half
    for id_ in range(from_, to+1):
        
        id_ = str(id_)
        left = id_[:int(len(id_)/2)]
        right = id_[int(len(id_)/2):]
        
        if left == right:
            invalid_ids += int(id_)

ans = invalid_ids

print(f"part 1 answer: {ans}")

######################### part 2 #########################

invalid_ids = 0

# for each range
for range_ in ranges:
    
    print(range_)
    from_, to = [int(x) for x in range_.split('-')]
    
    # for each id in the range
    for id_ in range(from_, to+1):
        
        id_ = str(id_)
        
        # start at longest sequence and work down to find repeat pattern
        for i in range(1,len(id_)):
            
            # if pattern repeated x times = id_, it's a match
            pattern = id_[:-i]
            repetitions = len(id_) / len(pattern)
            repetitions_int = int(repetitions)
            
            if repetitions_int == repetitions:
                full_pattern = pattern*repetitions_int
                
                if full_pattern == id_:
                    print('match!', pattern, '*', repetitions_int)
                    print(full_pattern)
                    invalid_ids += int(id_)
                    break


ans = invalid_ids

print(f"part 2 answer: {ans}")