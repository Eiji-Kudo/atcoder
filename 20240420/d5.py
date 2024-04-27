import sys
from collections import defaultdict, deque

# 標準入力から N と M を読み取る
N, M = map(int, input().split())

friends = defaultdict(set)
new_friendships = 0
processed = set()  # 処理済みの友達関係を記録するセット

# M 行分の友達関係を読み取る
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed に調整
    B -= 1  # 0-indexed に調整
    friends[A].add(B)
    friends[B].add(A)

# すべてのユーザーについてループ
for i in range(N):
    # 友達 j を調べる
    for j in friends[i]:
        if (i, j) not in processed and (j, i) not in processed:
            processed.add((i, j))
            processed.add((j, i))
            # j の友達 k が i の友達でない場合、新しい友達関係が成立
            for k in friends[j]:
                if k != i and k not in friends[i]:  # k は i と友達ではない
                    new_friendships += 1
                    friends[i].add(k)  # i の友達リストに k を追加
                    friends[k].add(i)  # k の友達リストに i を追加

print(f"{new_friendships}")
