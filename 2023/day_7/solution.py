input_data = open('day_7/input_1.txt', 'r').read().split('\n')
test_data = open('day_7/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import pandas as pd
data = input_data

## generate dataframe of hands and bigs. df seems the best way to rank hands
df = pd.DataFrame([d.split() for d in data])
df.columns = ['hand','bid']
df['bid'] = pd.to_numeric(df['bid'])

## based on possible hand, give a score
score_dict = {
    '5':6,
    '41':5,
    '32':4,
    '311':3,
    '221':2,
    '2111':1,
    '11111':0
    }

def get_score(a):
    groups = [str(a.count(i)) for i in ''.join(set(a))] ## count the occurence of each letter (''.join(set(a)) removes duplicate letters from the loop)
    groups.sort(reverse=True)
    groups = ''.join(groups)
    score = score_dict[groups]
    return score

## based on hand, give an alphabetic value for ordering
cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
values = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
values.reverse() ## makes ranking easier to reverse this
card_value_dict = dict(zip(cards,values))

def get_value(a):
    card_value = ''.join([card_value_dict[i] for i in a])
    return card_value

## applying scoring, and rank the hands, then calculate winnings
df['score'] = df['hand'].map(get_score)
df['value'] = df['hand'].map(get_value)
df['rank'] = df[['score','value']].apply(tuple,axis=1)\
             .rank(method='dense',ascending=True).astype(int)
df['winnings'] = df['rank']*df['bid']

ans = df['winnings'].sum()
print("part 1 answer: ", ans)

######################### part 2 #########################
import pandas as pd
data = input_data

## generate dataframe of hands and bigs. df seems the best way to rank hands
df = pd.DataFrame([d.split() for d in data])
df.columns = ['hand','bid']
df['bid'] = pd.to_numeric(df['bid'])

## based on possible hand, give a score
score_dict = {
    '5':6,
    '41':5,
    '32':4,
    '311':3,
    '221':2,
    '2111':1,
    '11111':0
    }

## alt score for using Js as jokers, we will still work out the true score as well
def get_score(a):
    if a == 'JJJJJ':
        score = 6
    else:
    ## remove Js and count Js
        hand_mod = a.replace('J','')
        j_count = a.count('J')
        groups = [a.count(i) for i in ''.join(set(hand_mod))] ## count the occurence of each letter (''.join(set(a)) removes duplicate letters from the loop)
        groups.sort(reverse=True)
        groups.insert(0,groups.pop(0)+j_count) ## take best hand and add the j_count on, then stick it back at the front
        groups = [str(i) for i in groups]
        groups = ''.join(groups)
        score = score_dict[groups]
    return score

## based on hand, give an alphabetic value for ordering
cards = ['A','K','Q','T','9','8','7','6','5','4','3','2','J'] ## moved J to the end of the line, as it's now weakest
values = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
values.reverse() ## makes ranking easier to reverse this
card_value_dict = dict(zip(cards,values))

def get_value(a):
    card_value = ''.join([card_value_dict[i] for i in a])
    return card_value

## applying scoring, and rank the hands, then calculate winnings
df['score'] = df['hand'].map(get_score)
df['value'] = df['hand'].map(get_value)
df['rank'] = df[['score','value']].apply(tuple,axis=1)\
             .rank(method='dense',ascending=True).astype(int)
df['winnings'] = df['rank']*df['bid']

ans = df['winnings'].sum()
print("part 2 answer: ", ans)
