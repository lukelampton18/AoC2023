input_file = open('input.txt', 'r')
inputs = input_file.read().splitlines()

games = [x.split(': ') for x in inputs]
powers = []

for x in games:      
    sets = x[1].split('; ')
    count = 1
    set = {
        'red': [0],
        'green': [0],
        'blue': [0]
    }
    for j in sets:      
        colors = j.split(', ')
        for k in colors:
            pair = k.split(' ')
            if pair[1] == 'red':
                set['red'].append(int(pair[0]))
            if pair[1] == 'green':
                set['green'].append(int(pair[0]))
            if pair[1] == 'blue':
                set['blue'].append(int(pair[0]))       
        count += 1
    red = max(set['red'])
    green = max(set['green'])
    blue = max(set['blue'])
    power = red * green * blue
    powers.append(power)

print(sum(powers))
        
