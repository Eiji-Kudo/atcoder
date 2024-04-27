from collections import deque

def max_freedom(grid, H, W):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 移動方向 (上, 下, 左, 右)
    visited = [[False] * W for _ in range(H)]  # 訪問済み配列をここで定義
    max_reachable = 0
    locked_cells_count = 0  # 磁石と隣接するマスのカウント

    def is_locked(r, c):
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
        local_locked_count = 0  # このBFSセッションでの隣接磁石マスのカウント

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if grid[nr][nc] == '.' and not local_visited[nr][nc]:
                        local_visited[nr][nc] = True
                        queue.append((nr, nc))
                        count += 1
                    elif grid[nr][nc] == '#':
                        local_locked_count += 1

        return count, local_locked_count

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and not visited[i][j] and not is_locked(i, j):
                visited[i][j] = True
                reachable, locked_count = bfs(i, j)
                locked_cells_count += locked_count
                if reachable > max_reachable:
                    max_reachable = reachable

    return max_reachable + locked_cells_count

# グリッドの定義
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 最大の自由度を計算
result = max_freedom(grid, H, W)
print(result)
