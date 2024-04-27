import sys
input = sys.stdin.read

def solve():
    data = input().split()
    N = int(data[0])  # ユーザの数
    M = int(data[1])  # 友達関係の数
    friendships = []

    index = 2
    for _ in range(M):
        A = int(data[index])
        B = int(data[index + 1])
        friendships.append((A, B))
        index += 2

    from collections import defaultdict

    graph = defaultdict(set)
    # グラフの構築
    for A, B in friendships:
        graph[A].add(B)
        graph[B].add(A)
    
    # 新たに友達関係を結ぶための操作回数をカウント
    operations = 0
    
    # 各友達関係を検討する
    for A, B in friendships:
        for C in graph[A]:
            if C != B:
                for D in graph[B]:
                    if D != A and D not in graph[A]:
                        graph[A].add(D)
                        graph[D].add(A)
                        operations += 1
                        break

    print(operations)

if __name__ == "__main__":
    solve()
