import sys
from collections import defaultdict

# 標準入力から N と M を読み取る
N, M = map(int, input().split())

friends = defaultdict(set)

# M 行分の友達関係を読み取る
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed に調整
    B -= 1  # 0-indexed に調整
    friends[A].add(B)
    friends[B].add(A)

for i in range(N):
    print(f"User {i+1}'s friends: {[f+1 for f in friends[i]]}")


new_friendships = 0
checked_pairs = set()  # 重複カウントを防ぐためにチェック済みのペアを記録

# すべてのユーザーについてループ
for i in range(N):
    # 友達 j を調べる
    for j in friends[i]:
        # i < j の条件で処理を実行することで重複を避ける
        if i != j:
            # j の友達 k が i の友達でない場合、新しい友達関係が成立
            common_friends = friends[i] & friends[j]  # i と j の共通の友達
            print(f"Common friends of {i+1} and {j+1}: {[f+1 for f in common_friends]}")
            potential_new_friends = friends[j] - friends[i] - {i}
            print(f"Potential new friends of {i+1}: {[f+1 for f in potential_new_friends]}")
            for k in potential_new_friends:
                if (i, k) not in checked_pairs and (k, i) not in checked_pairs:
                    print(f"New friendship established between {i+1} and {k+1}")
                    new_friendships += 1
                    checked_pairs.add((i, k))
                    checked_pairs.add((k, i))
print(new_friendships)