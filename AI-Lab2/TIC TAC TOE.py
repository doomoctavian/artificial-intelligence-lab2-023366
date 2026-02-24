# Tic-Tac-Toe Heuristic Function(023-352)
def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'

    lines = []

    lines.extend(board)

    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    def is_open(line, symbol):
        return opponent not in line if symbol == player else player not in line

    player_open = sum(is_open(line, player) for line in lines)
    opponent_open = sum(is_open(line, opponent) for line in lines)

    return player_open - opponent_open



if __name__ == "__main__":
    board = [
        ['X', 'O', ''],
        ['X', '', ''],
        ['', 'O', '']
    ]

    player = 'X'

    h_value = heuristic(board, player)
    print(f"Heuristic value e(P) for player {player}: {h_value}")