input_file = open('input.txt', 'r')
inputs = input_file.read().splitlines()

# print(inputs)

red = 12
green = 13
blue = 14

games = [x.split(': ') for x in inputs]
# sets = [x[1].split('; ') for x in games]

# print(sets)

for x in games:
    sets = x[1].split('; ')
    print(sets)
    for i in sets:
        print(i)
        count = 1

        all_sets = {}

        for j in i:
            set_number = count
            colors = j.split(', ')
            set = {
                'red': True,
                'green': True,
                'blue': True
            }
            print(j)
            for k in colors:
                pair = k.split(' ')
                if pair[1] == 'red':
                    if int(pair[0]) > red:
                        set['red'] = False
                if pair[1] == 'green':
                    if int(pair[0]) > green:
                        set['green'] = False
                if pair[1] == 'blue':
                    if int(pair[0]) > blue:
                        set['blue'] = False
            all_sets[f'set {set_number}'] = set
            count += 1
        # print(all_sets)
    print(sets)

        
