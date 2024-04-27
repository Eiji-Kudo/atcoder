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

# Count new friendships for each user
for i in range(N):
    all_second_friends = set()
    # Collect friends of friends of i
    for j in friends[i]:
        # Add friends of friends, excluding i and existing friends of i
        new_friends = friends[j] - friends[i] - {i}
        all_second_friends.update(new_friends)
    
    # Count the number of new friendships
    new_friendships += len(all_second_friends)
    for new_friend in all_second_friends:
        friends[i].add(new_friend)
        friends[new_friend].add(i)

print(f"{new_friendships}")
