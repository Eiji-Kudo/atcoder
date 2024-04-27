def check_winner(board, color):
    # 横、縦、斜めのラインをチェックして勝利条件を判断
    for i in range(3):
        if all(board[i][j] == color for j in range(3)):
            return True
        if all(board[j][i] == color for j in range(3)):
            return True
    if all(board[i][i] == color for i in range(3)):
        return True
    if all(board[i][2-i] == color for i in range(3)):
        return True
    return False

def find_immediate_win_move(board, color):
    # 即勝利が可能なマスを探す
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color
                if check_winner(board, color):
                    board[i][j] = 0
                    return (i, j)
                board[i][j] = 0
    return None

def solve_game():
    takahashi_points = 0
    aoki_points = 0
    board = [[0 for _ in range(3)] for _ in range(3)]
    turn_takahashi = True
    A = [list(map(int, input().split())) for _ in range(3)]

    # ターン毎の手順
    while any(0 in row for row in board):
        current_color = 1 if turn_takahashi else -1
        move_done = False

        # Step 1: 勝利できるマスがあれば即座に取る
        win_move = find_immediate_win_move(board, current_color)
        if win_move:
            i, j = win_move
            move_done = True

        # Step 2: 相手の勝利を阻止
        if not move_done:
            block_move = find_immediate_win_move(board, -current_color)
            if block_move:
                i, j = block_move
                move_done = True

        # Step 3: 中央マスを優先的に取る
        if not move_done:
            if board[1][1] == 0:
                i, j = 1, 1
                move_done = True

        # Step 4: 最大得点のマスを取る
        if not move_done:
            i, j = max(((i, j) for i in range(3) for j in range(3) if board[i][j] == 0),
                       key=lambda x: A[x[0]][x[1]])

        # マスを塗る
        board[i][j] = current_color
        current_points = A[i][j]
        if turn_takahashi:
            takahashi_points += current_points
        else:
            aoki_points += current_points

        # 勝利チェック
        if check_winner(board, current_color):
            return "Takahashi" if turn_takahashi else "Aoki"

        # 手番交代
        turn_takahashi = not turn_takahashi

    # 得点による勝者決定
    if takahashi_points > aoki_points:
        return "Takahashi"
    else:
        return "Aoki"

winner = solve_game()
print(winner)
