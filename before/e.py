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

def check_reach(board, color):
    # リーチ（2つ同じ色と1つ空白）があるマスの座標を返す
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color  # 仮にマスを塗る
                if check_winner(board, color):
                    board[i][j] = 0  # マスを元に戻す
                    return (i, j)
                board[i][j] = 0
    return None

def solve_game():
    takahashi_points = 0
    aoki_points = 0
    board = [[0 for _ in range(3)] for _ in range(3)]
    turn_takahashi = True
    A = [list(map(int, input().split())) for _ in range(3)]
    moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    moves.sort(key=lambda x: -A[x[0]][x[1]])

    for i, j in moves:
        if board[i][j] == 0:
            opponent_color = 1 if turn_takahashi else -1
            my_color = -1 if turn_takahashi else 1
            block_move = check_reach(board, opponent_color)
            if block_move:
                i, j = block_move
            else:
                # 他にリーチがない場合は最大値のマスを選択
                (i, j) = max(moves, key=lambda x: A[x[0]][x[1]])
                moves.remove((i, j))  # 選んだマスはリストから削除

            board[i][j] = my_color
            current_points = A[i][j]
            if turn_takahashi:
                takahashi_points += current_points
            else:
                aoki_points += current_points

            if check_winner(board, my_color):
                return "Takahashi" if turn_takahashi else "Aoki"

            # 手番を交代
            turn_takahashi = not turn_takahashi

    if takahashi_points > aoki_points:
        return "Takahashi"
    else:
        return "Aoki"

winner = solve_game()
print(winner)
