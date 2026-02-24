
# Blocks World Heuristic Calculation (023-352)

def calculate_heuristic(state, goal):
    goal_support = {}
    for stack in goal:
        for i, block in enumerate(stack):
            if i == 0:
                goal_support[block] = None 
            else:
                goal_support[block] = stack[i-1] 

    heuristic = 0

    for stack in state:
        for i, block in enumerate(stack):
            if i == 0:
                support = None 
            else:
                support = stack[i-1]  
            if goal_support.get(block) == support:
                heuristic += 1
            else:
                heuristic -= 1

    return heuristic

if __name__ == "__main__":
    initial_state = [['C', 'B'], ['A']]
    goal_state = [['A', 'B', 'C']]

    h_value = calculate_heuristic(initial_state, goal_state)
    print(f"Heuristic value E(P) for the current state: {h_value}")