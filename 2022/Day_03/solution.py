dir_ = "2022/day_03/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

######################### part 1 #########################
data = input_data

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

ans = 0
for d in data:
    a = d[len(d)//2:]
    b = d[:len(d)//2]
    
    item = list(set.intersection(set(i for i in a), set(i for i in b)))[0]
    ans += alphabet.index(item)+1
    
print(f"part 1 answer: {ans}")

######################### part 2 #########################

ans = 0
i = 0
while i+2 < len(data):
    a, b, c = data[i:i+3]
    badge = list(
        set.intersection(
            set(i for i in a),
            set(i for i in b),
            set(i for i in c)
            )
        )[0]
    
    ans += alphabet.index(badge)+1
    i+=3

print(f"part 2 answer: {ans}")