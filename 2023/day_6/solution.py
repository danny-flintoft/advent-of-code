input_data = open('day_6/input_1.txt', 'r').read().split('\n')
test_data = open('day_6/test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

times = [int(i) for i in data[0].split()[1:]]
distances = [int(i) for i in data[1].split()[1:]]

solutions_prod = 1
for time,distance in zip(times,distances):
    solutions = 0
    for hold_time in range(time+1):
        dist = hold_time*(time-hold_time)
        if dist > distance:
            solutions+=1
    solutions_prod*=solutions

print("part 1 answer: ", solutions_prod)

######################### part 2 #########################

## Brute Force Approach
time = int(data[0].replace(" ","").replace("Time:",""))
distance = int(data[1].replace(" ","").replace("Distance:",""))

solutions = 0
for hold_time in range(time+1):       
    dist = hold_time*(time-hold_time)
    if dist > distance:
        solutions+=1

print("part 2 answer: ", solutions)
## thank god for an easy day after yesterday! this was brute forced but could be solved more neatly with quadratic solution

## Quadratic Solution Approach
import math

time = int(data[0].replace(" ","").replace("Time:",""))
distance = int(data[1].replace(" ","").replace("Distance:",""))

def quadratic_solutions(a,b,c):
    c1 = math.sqrt(b**2-(4*a*c))/(2*a)
    x1 = int(b+c1)
    x2 = int(b-c1)
    solutions = x2-x1
    return solutions

solutions = quadratic_solutions(-1,time,-distance)
print("part 2 answer: ", solutions)