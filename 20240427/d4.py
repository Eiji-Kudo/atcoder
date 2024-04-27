from collections import deque

def max_freedom(grid, H, W):
    # 移動方向 (上, 下, 左, 右)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * W for _ in range(H)]
    max_reachable = 0

    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        count = 1  # 自分自身もカウントに含む

        print(f"Start BFS from ({start_row}, {start_col})")
        while queue:
            r, c = queue.popleft()
            print(f"  Visiting ({r}, {c}), queue size: {len(queue)}")
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == '.':
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    count += 1
                    print(f"    Move to ({nr}, {nc}), new queue size: {len(queue)}")
        print(f"  Total reachable from ({start_row}, {start_col}): {count}")
        return count

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and not visited[i][j]:
                # 磁石がない未訪問のマスからBFSを開始
                reachable = bfs(i, j)
                if reachable > max_reachable:
                    max_reachable = reachable
                print(f"Updated max reachable: {max_reachable}")

    return max_reachable

# グリッドの定義
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 最大の自由度を計算
result = max_freedom(grid, H, W)
print(f"Maximum freedom: {result}")
