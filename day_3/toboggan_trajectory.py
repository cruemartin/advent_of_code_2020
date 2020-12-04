def tree_colider(map, move_right, move_down):
    x = 0
    y = 0
    at_bottom = False
    trees = 0

    map_len = len(map)
    line_len = len(map[0])

    while not at_bottom:
        if y + move_right >= line_len:
            y = (y + move_right) % line_len
            x += move_down
        else:
            y = y + move_right
            x += move_down

        if x >= map_len or y >= line_len:
            at_bottom = True
            continue

        if map[x][y] == '#':
            trees +=1

    return trees



f = open('day_3\tree_map.txt', 'r')

map = f.read().split('\n')

f.close()


########### Part 1 ##########
print('1. Number of trees =', tree_colider(map, 3 ,1))

########## Part 2 ###########

slope = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2}
]

product = 1

for x in slope:
    product *=  tree_colider(map, x['right'], x['down'])

print('2. product of the slopes = ', product)
    