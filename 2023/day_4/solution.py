input_data = open('day_4/input_1.txt', 'r').read().split('\n')
test_data = open('day_4/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import re
data = input_data

## build function that gets the num lists (winners + my numbers)
def get_nums(a):       
    b = re.sub("Card [0-9]+: ","",a).replace("  "," ") ## remove the card info, and replace double spaces with single spaces
    b = b.split(" | ") ## split on pipe into winning nums & my nums
    winning_nums = b[0].split(" ") ## turn winning nums to list
    my_nums = b[1].split(" ") ## turn my nums to list
    return winning_nums, my_nums

## cycle through each card, get nums and compare overlap
score_count = 0
for a in data:
    winning_nums, my_nums = get_nums(a) ## get num lists
    match_count = len(set(winning_nums) & set(my_nums))  ## count overlap between both lists
    score = int(2**(match_count-1)) ## calculate score based on no. of matches
    score_count += score
    
print("part 1 answer: ", score_count)

######################### part 2 #########################

data = input_data

## combine the bits of part 1 to generate function that returns the matched count across winning/my numbers
def get_score(a):
    b = re.sub("Card [0-9]+: ","",a).replace("  "," ") ## remove the card info, and replace double spaces with single spaces
    b = b.split(" | ") ## split on pipe into winning nums & my nums
    winning_nums = b[0].split(" ") ## turn winning nums to list
    my_nums = b[1].split(" ") ## turn my nums to list
    match_count = len(set(winning_nums) & set(my_nums))  ## count overlap between both lists
    return match_count

## generate dict of card_ids and counts
card_dict = dict.fromkeys(range(1,len(data)+1),1)

## for each card, get matched count, and add 1 on to the dict value for each new card "won" from that card
for a in data:    
    print(card_dict)
    card_id = int(re.search(r'\d+', a).group()) ## get card id
    card_copies = card_dict[card_id]
    score = get_score(a) ## get score
    copies = list(range(card_id+1,card_id+score+1)) ## get list of copies won
    for i in copies:
        card_dict[i]+=1*card_copies ## add 1 for each new copie, multiplied by the number of iterations of this card

print("part 1 answer: ", sum(card_dict.values()))
