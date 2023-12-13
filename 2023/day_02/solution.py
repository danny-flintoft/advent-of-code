input_data = open('day_02/input_1.txt', 'r').read().split('\n')
test_data = open('day_02/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import re
data = input_data
data

max_cube_dict = {
                 'red':12,
                 'green':13,
                 'blue':14}

count = 0
for a in data:   
    game_id = int(re.search(r'\d+', a).group()) ## get game id
    colours = re.findall("[0-9]+ [a-z]+",a) ## get colour & amount strings
    colour = [re.sub("[^a-z]", "",i) for i in colours] ## get just colour
    amount = [int(re.search(r'\d+', i).group()) for i in colours] ## get just amount 
    breaker = [1 for col,amt in zip(colour,amount) if amt > max_cube_dict[col]] ## comapre amount to max amount for given colour
    if breaker == []: ## check if logic was broken
        count += game_id ## add non broken game_ids to count
        
print("answer to part 1:", count)

######################### part 2 #########################
import re
import pandas as pd
data = input_data

count = 0
for a in data:
    colours = re.findall("[0-9]+ [a-z]+",a) ## get colour & amount strings
    colour = [re.sub("[^a-z]", "",i) for i in colours] ## get just colour
    amount = [int(re.search(r'\d+', i).group()) for i in colours] ## get just amount
    df = pd.DataFrame({'colour':colour
                       ,'amount':amount}) ## create df of colours & amounts
    prod = int(df.groupby('colour').max().prod()) ## get prod of max for each colour
    count += prod
    
print("answer to part 2:", count)

