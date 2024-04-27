import sys
from collections import defaultdict, Counter

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
    print(f"Processing User {i+1} with current friends: {[f+1 for f in friends[i]]}")
    # i の友達の友達を集める
    for j in friends[i]:
        print(f"  Processing friend {j+1} of User {i+1}")
        all_second_friends.update(friends[j])
        print(f"  Updated potential new friends for User {i+1} after adding friends of {j+1}: {[f+1 for f in all_second_friends]}")
    
    # 自分自身と既存の友達を除外
    all_second_friends.discard(i)
    all_second_friends.difference_update(friends[i])
    print(f"  Valid new friends for User {i+1} after exclusions: {[f+1 for f in all_second_friends]}")

    # 新しい友達関係の数をカウント
    new_friendships += len(all_second_friends)
    print(f"  User {i+1} can establish {len(all_second_friends)} new friendships")
    for new_friend in all_second_friends:
        print(f"    Establishing new friendship between User {i+1} and User {new_friend+1}")
        friends[i].add(new_friend)
        friends[new_friend].add(i)
        print(f"    Updated friend list for User {i+1}: {[f+1 for f in friends[i]]}")
        print(f"    Updated friend list for User {new_friend+1}: {[f+1 for f in friends[new_friend]]}")

print(f"Total new friendships established: {new_friendships}")
