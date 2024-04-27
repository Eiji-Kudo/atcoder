from collections import deque

def max_freedom(grid, H, W):
    # 移動方向 (上, 下, 左, 右)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * W for _ in range(H)]  # 訪問済み配列をここで定義
    max_reachable = 0

    def is_locked(r, c):
        # 隣接するマスに磁石があるかどうかチェック
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '#':
                return True
        return False

    def bfs(start_row, start_col):
        local_visited = [[False] * W for _ in range(H)]  # 各BFSごとに訪問状態をリセット
        queue = deque([(start_row, start_col)])
        local_visited[start_row][start_col] = True
        count = 1  # 自分自身もカウントに含む

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not local_visited[nr][nc] and grid[nr][nc] == '.':
                    if not is_locked(nr, nc):
                        local_visited[nr][nc] = True
                        queue.append((nr, nc))
                        count += 1
        return count

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and not visited[i][j]:
                if not is_locked(i, j):
                    visited[i][j] = True
                    reachable = bfs(i, j)
                    if reachable > max_reachable:
                        max_reachable = reachable

    return max_reachable

# グリッドの定義
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 最大の自由度を計算
result = max_freedom(grid, H, W)
print(f"{result}")
