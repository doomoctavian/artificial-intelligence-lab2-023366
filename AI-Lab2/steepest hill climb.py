
# Steepest-Ascent Hill Climbing for 8-Puzzle(023-352)


import copy

moves = [(-1,0), (1,0), (0,-1), (0,1)]

goal_state = [[1,2,3],[4,5,6],[7,8,0]]

def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                h += 1
    return h

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i,j)
    return None

def successors(state):
    succ = []
    x, y = find_zero(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            succ.append(new_state)
    return succ

def hill_climbing(initial_state):
    current = initial_state
    path = [current]
    current_h = heuristic(current)

    while True:
        succ = successors(current)

        succ_h = [heuristic(s) for s in succ]
        min_h = min(succ_h)
        if min_h >= current_h:

            break
        index = succ_h.index(min_h)
        current = succ[index]
        current_h = min_h
        path.append(current)
        if current_h == 0:
            break

    return path


def print_state(state):
    for row in state:
        print(row)
    print("---")


if __name__ == "__main__":
    initial_state = [[1,2,3],[4,0,6],[7,5,8]]

    print("Initial State:")
    print_state(initial_state)

    path = hill_climbing(initial_state)

    print(f"Number of steps: {len(path)-1}\n")
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print_state(state)

    if heuristic(path[-1]) == 0:
        print("Goal state reached!")
    else:
        print("Stopped at local maximum (goal not reached).")