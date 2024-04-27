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

for i in range(N):
    current_friends = list(friends[i])
    print(f"Current user: {i+1}, Current friends: {[f+1 for f in current_friends]}")
    for j in current_friends:
        potential_new_friends = list(friends[j])
        print(f"Friend: {j+1}, Potential new friends: {[f+1 for f in potential_new_friends]}")
        for k in potential_new_friends:
            if k != i and k not in friends[i]:
                if (i, k) not in considered_pairs and (k, i) not in considered_pairs:
                    new_friendships += 1
                    print(f"New friendship established: {i+1} and {k+1}")
                    friends[i].add(k)
                    friends[k].add(i)
                    considered_pairs.add((i, k))
                    considered_pairs.add((k, i))
print(f"Total new friendships: {new_friendships}")