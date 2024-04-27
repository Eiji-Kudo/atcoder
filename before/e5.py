def check_winner(board, color):
    # Check rows, columns, and diagonals for a win condition
    for i in range(3):
        if all(board[i][j] == color for j in range(3)):
            print(f"Winner found on row {i} for color {color}")
            return True
        if all(board[j][i] == color for j in range(3)):
            print(f"Winner found on column {i} for color {color}")
            return True
    if all(board[i][i] == color for i in range(3)):
        print("Winner found on main diagonal for color {color}")
        return True
    if all(board[i][2-i] == color for i in range(3)):
        print("Winner found on secondary diagonal for color {color}")
        return True
    return False

def find_immediate_win_move(board, color):
    # Find a move that immediately results in a win
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color
                if check_winner(board, color):
                    board[i][j] = 0
                    print(f"Immediate win move found at ({i}, {j}) for color {color}")
                    return (i, j)
                board[i][j] = 0
    return None

def find_block_move(board, color):
    # Find a move that blocks the opponent's immediate win
    block = find_immediate_win_move(board, -color)
    if block:
        print(f"Blocking opponent move at {block}")
    return block

def find_create_reach_move(board, color, A):
    # Find the best move that creates a potential win (reach) for the next move
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color
                if check_reach(board, color):
                    score = A[i][j]
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                        print(f"Potential reach move at ({i}, {j}) with score {score}")
                board[i][j] = 0
    return best_move

def check_reach(board, color):
    # Check for reach condition without immediate win
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color
                if check_winner(board, color):
                    board[i][j] = 0
                    continue
                board[i][j] = 0
                if find_immediate_win_move(board, color):
                    return True
    return False

def solve_game():
    takahashi_points = 0
    aoki_points = 0
    board = [[0 for _ in range(3)] for _ in range(3)]
    turn_takahashi = True
    A = [list(map(int, input().split())) for _ in range(3)]

    while any(0 in row for row in board):
        current_color = 1 if turn_takahashi else -1

        # Step 1: Check if current player can win immediately
        win_move = find_immediate_win_move(board, current_color)
        if win_move:
            i, j = win_move
        else:
            # Step 2: Block opponent's immediate winning move
            block_move = find_block_move(board, current_color)
            if block_move:
                i, j = block_move
            else:
                # Step 3: Create a reach if possible
                create_reach = find_create_reach_move(board, current_color, A)
                if create_reach:
                    i, j = create_reach
                else:
                    # Step 4: Choose the highest scoring move
                    i, j = max(((i, j) for i in range(3) for j in range(3) if board[i][j] == 0),
                               key=lambda x: A[x[0]][x[1]])
                    print(f"Choosing highest scoring move at ({i}, {j}) with score {A[i][j]}")

        board[i][j] = current_color
        current_points = A[i][j]
        if turn_takahashi:
            takahashi_points += current_points
        else:
            aoki_points += current_points

        print(f"Move at ({i}, {j}) by {'Takahashi' if turn_takahashi else 'Aoki'}, Score: {current_points}")

        if check_winner(board, current_color):
            winner = "Takahashi" if turn_takahashi else "Aoki"
            print(f"{winner} wins!")
            return winner

        # Toggle turns
        turn_takahashi = not turn_takahashi

    # Final score comparison if no winner by lines
    if takahashi_points > aoki_points:
        return "Takahashi"
    else:
        return "Aoki"

winner = solve_game()
print(winner)
