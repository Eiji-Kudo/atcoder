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

def find_reach_move(board, color):
    # 2つ同じ色と1つ空白のラインを探す（リーチを作る）
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color  # 仮にマスを塗る
                if check_winner(board, color):
                    board[i][j] = 0  # マスを元に戻す
                    return (i, j)
                board[i][j] = 0
    return best_move

def find_best_potential_move(board, A, color):
    # 最も有望なマスを選択する（未来のリーチの可能性を考える）
    potential_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = color
                if any(
                    sum(board[x][y] == color for y in range(3)) == 2 or
                    sum(board[y][x] == color for y in range(3)) == 2 or
                    sum(board[k][k] == color for k in range(3)) == 2 or
                    sum(board[k][2-k] == color for k in range(3)) == 2
                for x in range(3)):
                    potential_moves.append((i, j, A[i][j]))
                board[i][j] = 0
    # 最大得点のマスを選ぶ
    return max(potential_moves, key=lambda x: x[2]) if potential_moves else None

def solve_game():
    takahashi_points = 0
    aoki_points = 0
    board = [[0 for _ in range(3)] for _ in range(3)]
    turn_takahashi = True
    A = [list(map(int, input().split())) for _ in range(3)]

    while True:
        moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
        if not moves:
            break

        # リーチがあるか確認
        color = 1 if turn_takahashi else -1
        block_move = find_reach_move(board, -color)
        if block_move:
            i, j = block_move
        else:
            # リーチを作れる最適なマスを探す
            potential_move = find_best_potential_move(board, A, color)
            if potential_move:
                i, j, _ = potential_move
            else:
                # 最大得点のマスを選ぶ
                i, j, _ = max([(i, j, A[i][j]) for i, j in moves], key=lambda x: x[2])

        board[i][j] = color
        current_points = A[i][j]
        if turn_takahashi:
            takahashi_points += current_points
        else:
            aoki_points += current_points

        if check_winner(board, color):
            return "Takahashi" if turn_takahashi else "Aoki"

        # 手番を交代
        turn_takahashi = not turn_takahashi

    if takahashi_points > aoki_points:
        return "Takahashi"
    else:
        return "Aoki"

winner = solve_game()
print(winner)
