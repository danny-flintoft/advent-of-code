dir_ = "2024/day_02/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')
data = input_data

## get reports as separate list of ints
reports = []
for d in data:
    report = [int(x) for x in d.split()]
    reports.append(report)
    
######################### part 1 #########################

## def function to take difference of each elements vs neighbour
def get_diffs(report):
    diffs = []
    for i in range(len(report)-1):
       diff = report[i+1] - report[i]
       diffs.append(diff)        
    abs_diffs = [abs(x) for x in diffs]
    return diffs, abs_diffs

## def function to check if report differences violate any rules
def check_report(report):
    diffs, abs_diffs = get_diffs(report)
    rule_1 = min(diffs) < 0 and max(diffs) > 0
    rule_2 = max(abs_diffs) > 3 or min(abs_diffs) < 1
    violation = rule_1 or rule_2
    return violation

## run across all reports
ans = 0
for report in reports:
    violation = check_report(report)
    if not violation:
        ans+=1
    
print("part 1 answer:", ans)

######################### part 2 #########################

## run for all variants of a report
ans = 0
for report in reports:
    variants = [report[:i] + report[i+1:] for i in range(len(report))]
    
    approved = 0
    for variant in variants:
        violation = check_report(variant)
        if not violation:
            approved = 1
            break
    ans+=approved

print("part 2 answer:", ans)
