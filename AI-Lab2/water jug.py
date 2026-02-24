# Water Jug Problem using DFS and BFS(023-352)

from collections import deque

class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, current_state, goal_state):
        return current_state == goal_state

    def successor(self, state):
        x, y = state
        successors = []

        # Fill the 4-liter jug
        successors.append((4, y))

        # Fill the 3-liter jug
        successors.append((x, 3))

        # Empty the 4-liter jug
        successors.append((0, y))

        # Empty the 3-liter jug
        successors.append((x, 0))

        # Pour water from 4L jug to 3L jug
        transfer = min(x, 3 - y)
        successors.append((x - transfer, y + transfer))

        # Pour water from 3L jug to 4L jug
        transfer = min(y, 4 - x)
        successors.append((x + transfer, y - transfer))

        return successors


def generate_path(closed, goal_state):
    
    path = []
    state = goal_state

    while state is not None:
        path.append(state)
        state = closed[state]

    path.reverse()
    return path


def bfs(problem):
    queue = deque()
    queue.append(problem.initial_state)

    closed = {}
    closed[problem.initial_state] = None

    while queue:
        current = queue.popleft()

        if problem.goal_test(current, problem.goal_state):
            return generate_path(closed, current)

        for child in problem.successor(current):
            if child not in closed:
                closed[child] = current
                queue.append(child)

    return None


def dfs(problem):
    stack = []
    stack.append(problem.initial_state)

    closed = {}
    closed[problem.initial_state] = None

    while stack:
        current = stack.pop()

        if problem.goal_test(current, problem.goal_state):
            return generate_path(closed, current)

        for child in problem.successor(current):
            if child not in closed:
                closed[child] = current
                stack.append(child)

    return None

if __name__ == "__main__":
    initial_state = (4, 0)  
    goal_state = (2, 0)     
    problem = WaterJug(initial_state, goal_state)

    print("BFS Solution Path:")
    bfs_path = bfs(problem)
    for step in bfs_path:
        print(step)

    print("\nDFS Solution Path:")
    dfs_path = dfs(problem)
    for step in dfs_path:
        print(step)