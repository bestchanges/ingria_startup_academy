
import copy

inhabit_area = [
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
]

def display_area_state(area):
    for j in range(len(area)):
        width = len(area[j])
        line = ""
        for i in range(width):
            if area[j][i] > 0:
                line += "O"
            else:
                line += "_"
        print(line)

def life_iteration(area):
    height = len(area)
    new_area = copy.deepcopy(area)
    for j in range(height):
        width = len(area[j])
        for i in range(width):
            neigbors = 0
            # let's count neighbors
            for j1 in range(j-1, j+2):
                if j1 < 0 or j1 >= height:
                    # out of the area
                    continue
                for i1 in range(i-1, i+2):
                    if i1 < 0 or i1 >= width:
                        # out of the area
                        continue
                    if i1 == i and j1 == j:
                        # do not count cell itself
                        continue
                    if area[j1][i1] > 0:
                        neigbors += 1
            if neigbors == 3:
                # start new life (or continue to live)
                new_area[j][i] = 1
            elif neigbors == 2:
                # keep living if already alive
                new_area[j][i] = area[j][i]
            else:
                # otherwise - die
                new_area[j][i] = 0
    return new_area

while True:
    display_area_state(inhabit_area)
    print("===== Press enter to continue, write 'exit' to finish ========")
    command = input()
    if command == 'exit':
        exit()
    inhabit_area = life_iteration(inhabit_area)
