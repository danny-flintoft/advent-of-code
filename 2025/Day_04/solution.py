dir_ = "2025/day_04/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

# build the grid of rolls of paper
X = len(data[0])
Y = len(data)
grid_dict = dict()

for x in range(X):
    for y in range(Y):
        grid_dict[(x,y)] = data[y][x]

# define function to add two tuple coordinates
def add_coords(t1, t2):
    return tuple(sum(x) for x in zip(t1, t2))

# define function to get all adjacent cells to a position
def get_adjacents(pos):
    directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    adjacents = [add_coords(pos, d) for d in directions]
    adjacents_filtered = [a for a in adjacents 
                          if a[0] >= 0 and a[0] < X 
                          and a[1] >= 0 and  a[1] < Y]
    return adjacents_filtered

# define function to search grid and remove all reachable rolls
def remove_rolls(grid_dict):
    iterated_dict = grid_dict.copy()
    rolls_removed = 0
    for x in range(X):
        for y in range(Y):
            pos = (x,y)
            if grid_dict[pos] == '@':
                adjacents = get_adjacents(pos)
                rolls_of_paper = \
                sum(1 for a in adjacents if grid_dict[a] == '@')
                if rolls_of_paper < 4:
                    iterated_dict[pos] = '.'
                    rolls_removed += 1
    return iterated_dict, rolls_removed

######## part 1 ########

# remove rolls once for part 1
_, ans = remove_rolls(grid_dict)
print(f"part 1 answer: {ans}")

######## part 2 ########

# remove rolls as many times as needed for part 2 (until no are rolls removed)
ans = 0
rolls_removed = 1
while rolls_removed != 0:
    grid_dict, rolls_removed = remove_rolls(grid_dict)
    ans += rolls_removed

print(f"part 2 answer: {ans}")