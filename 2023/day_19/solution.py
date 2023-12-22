input_data = open('day_19/input_1.txt', 'r').read().split('\n')
test_data = open('day_19/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
import re
debug = False
data = input_data
data.remove('')
workflows = [row for row in data if row[0] != '{']
parts = [row for row in data if row[0] == '{']

## process workflows into a dictionary. Key = workflow_name, value = list of condition/destination tuples
workflow_dict = {}
for a in workflows:
    workflow_name,conditions=a[:-1].split('{')
    conditions = conditions.split(',')
    conditions = [tuple(con) if len(con)==2 else ('True',con[0]) for con in [condition.split(':') for condition in conditions]]
    workflow_dict[workflow_name] = conditions

## process parts into a list of Part class objects
class Part:
    def __init__(self,x,m,a,s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    def get_xmas(self):
        return self.x,self.m,self.a,self.s
   
part_list = []
for part in parts:
    part_list.append(Part(*[int(re.findall("[0-9]+",x)[0]) for x in part.split(',')]))

## do the stuff
score = 0
for part in part_list:
    x,m,a,s = part.get_xmas()
    workflow_name = 'in'
    finished = 0
    while finished == 0:
        for rule in workflow_dict[workflow_name]:
            condition = rule[0]
            action = rule[1]
            if eval(condition):
                if debug:
                    print('condition met')
                if action == 'R':
                    finished = 1
                    if debug:
                        print('rejected')
                elif action == 'A':
                    score+=(x+m+a+s)
                    finished = 1
                    if debug:
                        print('accepted')
                else:
                    workflow_name = action
                    if debug:
                        print('move to workflow',action)
                break
            else:
                if debug:
                    print('condition not met') 
    
print("part 1 answer:", score)

######################### part 2 #########################

## general approach is to start at the 'A' and work backwards to see what batch would have landed here
## then count up permutations in the accepted batches

## define function augment our batch based on the rule
## rule can either be accepted or rejected, depending on where in the journey we are
def reduce_batch(batch,rule):
    if rule == 'True':
        pass
    else:
        ## get components of the rule
        category = rule[0]
        sign = rule[1]
        amount = int(rule[2:])
        ## get relevant range in current batch
        batch_range = batch[cat_dict[category]]
        ## split the batch accordingly
        if sign == '<':
            filtered_val = (batch_range[0],min(batch_range[1],amount-1))
            new_val = (max(amount,batch_range[0]),batch_range[1])
        else:
            filtered_val = (max(batch_range[0],amount+1),batch_range[1])
            new_val = (batch_range[0],min(amount,batch_range[1]))
        if initial_rule == 1:
            batch[cat_dict[category]] = filtered_val 
        else:
            batch[cat_dict[category]] = new_val 
    return batch


## build dict of which workflow (value) leads to which workflow (key)
## this is used to work backwards through the workflows until we arrive at the start ('in')
workflow_mapping = {}
for key,values in workflow_dict.items():
    for value in values:
        if value[1] in ['A','R']:
            pass
        else:
            workflow_mapping[value[1]] = key

## maintina a list of accepted batches, as well as journeys we have completed and workflows that are left to check
accepted = [] ## accepted batches
completed = [] ## compelted 'A' points in workflows - this list is used to prevent us checking the same 'A' multiple times
workflows = list(workflow_dict.keys()) ## all workflows to check - these get removed througout the loop as they are exhausted

while len(workflows) != 0:
    workflow_name = workflows[0]
    batch = [(1,4000)]*4 ## generate a starting batch of all possible values
    A_rule = 1 ## used to determine what point in a workflow we are starting from
    ## check to see if the given workflow has any A values left that have not already been checked (so are in the completed list)
    rules = workflow_dict[workflow_name]
    A_count = len([i for i in range(len(rules)) if rules[i][1] == 'A' and (workflow_name,i) not in completed])
    if A_count == 0:
        workflows.remove(workflow_name)
        continue ## starts a new loop if this workflow has been exhausted
    else:
        while 1==1: ## until we break
            initial_rule = 1 ## if it's the first rule (the one that lands us at A, or routes us to a new workflow) we accept the rule, else reject
            rules = workflow_dict[workflow_name]
            if A_rule == 1: ## if we are starting a new loop, and therefore looking for an 'A' to work back from
                start_index = [i for i in range(len(rules)) if rules[i][1] == 'A' and (workflow_name,i) not in completed][0] ## find the A in the rule set and start here
                index_list = list(range(start_index+1))[::-1]
                completed.append((workflow_name,start_index))
            else: ## else we are mid way through a journey, and therefore starting from wherever we would get directed to the previous workflow
                start_index = [i for i in range(len(rules)) if rules[i][1] == prev_workflow_name][0] ## find the previous workflow name in the rule set and start here
                index_list = list(range(start_index+1))[::-1]
            for index in index_list: ## cycle through the rules in a workflow, in reverse order, reducing the batch accordingly
                rule = rules[index][0]
                batch = reduce_batch(batch,rule)
                initial_rule = 0 ## after 1st (and any) we are no longer on inital rule
                A_rule = 0 ## also no longer on the A_rule
            if workflow_name == 'in': ## if it's the final workflow, and we have exhausted all rules, accept the batch!
                accepted.append(batch)
                break
            else: ## else we still have other workflows to work back through until we reach the starting workflow ('in')
                prev_workflow_name = workflow_name
                workflow_name = workflow_mapping[workflow_name]   

## count up the permutations in all our batches                
accpeted_count = 0   
for batch in accepted:
     prod = 1
     ranges = [a[1]-a[0]+1 for a in batch]
     for val in ranges:
         prod = prod*val
     accpeted_count += prod

print("part 2 answer:", accpeted_count)