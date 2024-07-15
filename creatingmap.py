map = []

for i in range(400):
    map.append('.')
    for j in range(200):


        #przypisywanie x i y
        x = float(j) #x równa się skali naszej mapy
        y = int(20/(x+1)/(x+1) + 0.08*x*x - 10*x + 320) # y 
        if y == i and x == j:
            map[i] += '*'
        else:
            map[i] += ' '
    map[i] += '.'

for i in range(len(map), 0, -1):
    print(map[i-1])