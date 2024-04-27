def check_winner(board, color):
    # 横のラインをチェック
    for row in board:
        if all(cell == color for cell in row):
            return True
    
    # 縦のラインをチェック
    for col in range(3):
        if all(board[row][col] == color for row in range(3)):
            return True
    
    # 斜めのラインをチェック
    if all(board[i][i] == color for i in range(3)) or all(board[i][2-i] == color for i in range(3)):
        return True

    return False

def solve_game():
    # プレイヤーの得点
    takahashi_points = 0
    aoki_points = 0
    
    # ゲームボードの初期化（0: 白, 1: 赤, -1: 青）
    board = [[0 for _ in range(3)] for _ in range(3)]
    
    # ターン管理（True: 高橋君の手番, False: 青木君の手番）
    turn_takahashi = True
    
    # 標準入力からデータを受け取る
    A = [list(map(int, input().split())) for _ in range(3)]
    
    # 全てのマスを得点の高い順に選択
    moves = [(i, j) for i in range(3) for j in range(3)]
    moves.sort(key=lambda x: -A[x[0]][x[1]])
    
    for i, j in moves:
        if board[i][j] == 0:
            if turn_takahashi:
                board[i][j] = 1
                takahashi_points += A[i][j]
                if check_winner(board, 1):
                    return "Takahashi"
            else:
                board[i][j] = -1
                aoki_points += A[i][j]
                if check_winner(board, -1):
                    return "Aoki"
            
            # 手番を交代
            turn_takahashi = not turn_takahashi
    
    # すべてのマスが選択された後、得点が高い方が勝者
    if takahashi_points > aoki_points:
        return "Takahashi"
    else:
        return "Aoki"

# ゲームの実行と勝者の出力
winner = solve_game()
print(winner)
