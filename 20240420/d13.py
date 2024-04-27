import sys
from collections import defaultdict

# 標準入力から N と M を読み取る
N, M = map(int, input().split())

friends = defaultdict(set)
new_friendships = 0

# M 行分の友達関係を読み取る
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed に調整
    B -= 1  # 0-indexed に調整
    friends[A].add(B)
    friends[B].add(A)

# 各ユーザーに対して新しい友達関係をカウント
for i in range(N):
    all_second_friends = set()
    # i の友達の友達を集める
    for j in friends[i]:
        # 友達の友達を追加するが、i自身とiの既存の友達は除外
        new_friends = friends[j] - friends[i] - {i}
        all_second_friends.update(new_friends)
    
    # 新しい友達関係の数をカウント
    for new_friend in all_second_friends:
        if new_friend not in friends[i]:
            friends[i].add(new_friend)
            friends[new_friend].add(i)
            new_friendships += 1  # 新しい友達関係が確立されたらカウンターをインクリメント

print(f"{new_friendships}")
