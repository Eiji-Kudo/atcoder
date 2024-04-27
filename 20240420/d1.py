import sys
from collections import defaultdict

# 標準入力から N と M を読み取る
N, M = map(int, sys.stdin.readline().split())

friends = defaultdict(set)

# M 行分の友達関係を読み取る
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    A -= 1  # 0-indexed に調整
    B -= 1  # 0-indexed に調整
    friends[A].add(B)
    friends[B].add(A)

new_friendships = 0

# すべてのユーザーについてループ
for i in range(N):
    # 友達 j を調べるために一時リストを作成
    temp_friends_i = list(friends[i])
    for j in temp_friends_i:
        if i < j:  # 重複カウントを防ぐため i < j の場合のみ考慮
            # j の友達 k が i の友達でない場合、新しい友達関係が成立
            temp_friends_j = list(friends[j])
            for k in temp_friends_j:
                if k != i and k not in friends[i]:  # k は i と友達ではない
                    new_friendships += 1
                    # 新しい友達関係を登録（後で重複カウントしないように）
                    friends[i].add(k)
                    friends[k].add(i)

print(new_friendships)
