# using A* algorithm(023-352)
import heapq
class PuzzleSolver:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
    
    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    
    def get_neighbors(self, state):
        neighbors = []
        row, col = self.find_blank(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]
                new_state[row][col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[row][col]
                neighbors.append(new_state)
        return neighbors
    
    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile != 0:
                    for gi in range(3):
                        for gj in range(3):
                            if self.goal[gi][gj] == tile:
                                distance += abs(i - gi) + abs(j - gj)
        return distance
    
    def state_to_string(self, state):
        return str(state)
    
    def solve(self):
        print("Solving puzzle using A* algorithm...")
        start_h = self.manhattan_distance(self.start)
        heap = [(start_h, 0, self.start, [])]
        visited = set()
        nodes_explored = 0
        
        while heap:
            f_score, g_score, current, path = heapq.heappop(heap)
            nodes_explored += 1
            # Check if goal reached
            if current == self.goal:
                print(f"Solution found!")
                print(f"Nodes explored: {nodes_explored}")
                print(f"Steps needed: {g_score}")
                return path + [current]

            state_str = self.state_to_string(current)
            if state_str in visited:
                continue
            visited.add(state_str)

            for neighbor in self.get_neighbors(current):
                neighbor_str = self.state_to_string(neighbor)
                
                if neighbor_str not in visited:
                    new_g = g_score + 1
                    new_h = self.manhattan_distance(neighbor)
                    new_f = new_g + new_h
                    heapq.heappush(heap, (new_f, new_g, neighbor, path + [current]))
        print("No solution found!")
        return None
    
    def print_state(self, state):
        for row in state:
            print(" ".join(str(tile) if tile != 0 else "_" for tile in row))
        print()
    
    def print_solution(self, solution):
        if not solution:
            print("No solution to display")
            return
        print("\nSolution Steps:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            self.print_state(state)

if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    print("8-Puzzle Solver using A* Algorithm")
    print("\nInitial State:")
    solver = PuzzleSolver(start, goal)
    solver.print_state(start)
    print("Goal State:")
    solver.print_state(goal)
    
    solution = solver.solve()
    if solution:
        solver.print_solution(solution)