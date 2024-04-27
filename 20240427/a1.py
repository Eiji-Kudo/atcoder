def minimum_runs_for_win(A, B):
    # チーム高橋とチーム青木の得点をそれぞれ合計する
    sum_takahashi = sum(A)
    sum_aoki = sum(B)
    
    # 勝つためにはチーム青木が9回裏に取る必要のある最小の点数を計算する
    # これはチーム高橋の合計得点より1点多くなるようにする
    needed_points = sum_takahashi - sum_aoki + 1
    
    # 必要な得点を出力する
    return needed_points


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(minimum_runs_for_win(A, B))


