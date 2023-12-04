input_file = open('input.txt', 'r')
inputs = input_file.read().splitlines()

# print(inputs)

red = 12
green = 13
blue = 14

games = [x.split(': ') for x in inputs]
# sets = [x[1].split('; ') for x in games]

# print(sets)

counter = 1
game_valid = []

for x in games:
    valid = True       
    sets = x[1].split('; ')
    print(sets)
    count = 1
    all_sets = {}
    for j in sets:
        print(j)
        set_number = count
        colors = j.split(', ')
        set = {
            'red': True,
            'green': True,
            'blue': True
        }
        print(colors)
        for k in colors:
            print(k)
            pair = k.split(' ')
            if pair[1] == 'red':
                if int(pair[0]) > red:
                    set['red'] = False
                    valid = False
            if pair[1] == 'green':
                if int(pair[0]) > green:
                    set['green'] = False
                    valid = False
            if pair[1] == 'blue':
                if int(pair[0]) > blue:
                    set['blue'] = False
                    valid = False
        all_sets[f'set {set_number}'] = set        
        count += 1
    game_valid.append((counter,valid))
    counter += 1

print(game_valid)
sums = [x[0] for x in game_valid if x[1] == True]     
print(sums)   

print(sum(sums))

        
