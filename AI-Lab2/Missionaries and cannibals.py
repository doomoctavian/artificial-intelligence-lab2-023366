# Missionaries and Cannibals Problem(023-352)
from collections import deque
class MissionariesCannibals:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, state):
        return state == self.goal_state

    def is_legal(self, state):
        M_left, C_left, _ = state
        M_right = 3 - M_left
        C_right = 3 - C_left

        if not (0 <= M_left <= 3 and 0 <= C_left <= 3):
            return False

        if M_left > 0 and M_left < C_left:
            return False

        if M_right > 0 and M_right < C_right:
            return False
        return True

    def successor(self, state):
        M_left, C_left, boat = state
        moves = []
        boat_moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for m, c in boat_moves:
            if boat == 'L':  
                new_state = (M_left - m, C_left - c, 'R')
            else:           
                new_state = (M_left + m, C_left + c, 'L')

            if self.is_legal(new_state):
                moves.append(new_state)
        return moves


def generate_path(parent, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path


def bfs(problem):
    queue = deque([problem.initial_state])
    parent = {problem.initial_state: None}

    while queue:
        current = queue.popleft()

        if problem.goal_test(current):
            return generate_path(parent, current)

        for child in problem.successor(current):
            if child not in parent:
                parent[child] = current
                queue.append(child)
    return None


def dfs(problem):
    stack = [problem.initial_state]
    parent = {problem.initial_state: None}

    while stack:
        current = stack.pop()

        if problem.goal_test(current):
            return generate_path(parent, current)

        for child in problem.successor(current):
            if child not in parent:
                parent[child] = current
                stack.append(child)
    return None

if __name__ == "__main__":
    initial_state = (3, 3, 'L')
    goal_state = (0, 0, 'R')
    problem = MissionariesCannibals(initial_state, goal_state)

    print("\nBFS SOLUTION")
    bfs_path = bfs(problem)
    for i, step in enumerate(bfs_path):
        M_left, C_left, boat = step
        M_right = 3 - M_left
        C_right = 3 - C_left
        print(f"Step {i}: Left(M={M_left},C={C_left}) Right(M={M_right},C={C_right}) Boat={boat}")

    print("\n DFS SOLUTION ")
    dfs_path = dfs(problem)
    for i, step in enumerate(dfs_path):
        M_left, C_left, boat = step
        M_right = 3 - M_left
        C_right = 3 - C_left
        print(f"Step {i}: Left(M={M_left},C={C_left}) Right(M={M_right},C={C_right}) Boat={boat}")

    print("\n GOAL ACHIEVED \n")