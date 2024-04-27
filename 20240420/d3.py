import sys
from collections import defaultdict

# 標準入力から N と M を読み取る
N, M = map(int, input().split())

friends = defaultdict(set)
new_friendships = 0
considered_pairs = set()  # カウント済みのペアを記録するセット

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
        # j の友達 k が i の友達でない場合、新しい友達関係が成立
        for k in friends[j]:
            if k != i and k not in friends[i]:  # k は i と友達ではない
                # 重複チェック: (i, k) または (k, i) が既に考慮されていないか確認
                if (i, k) not in considered_pairs and (k, i) not in considered_pairs:
                    new_friendships += 1  # 新しい友達関係をカウント
                    considered_pairs.add((i, k))  # 重複を避けるためペアを記録
                    considered_pairs.add((k, i))  # 逆方向も記録

print(f"Total new friendships: {new_friendships}")
