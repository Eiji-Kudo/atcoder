import sys
from collections import deque

def bfs(grid, start_row, start_col, H, W):
    print(f"Starting BFS from ({start_row}, {start_col})")  # Debug print
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上, 下, 左, 右
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])
    count = 1  # 起点マスも含めるため、1 から始める

    while queue:
        r, c = queue.popleft()
        print(f"  Visiting ({r}, {c})")  # Debug print
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.' and (nr, nc) not in visited:
                # 磁石が隣接するかチェック
                magnet_nearby = any(0 <= nr + ddr < H and 0 <= nc + ddc < W and grid[nr + ddr][nc + ddc] == '#' for ddr, ddc in directions)
                if not magnet_nearby:
                    print(f"    Adding ({nr}, {nc}) to visited")  # Debug print
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    count += 1
    return count

def main():
    H, W = map(int, sys.stdin.readline().strip().split())
    grid = [sys.stdin.readline().strip() for _ in range(H)]

    max_degree_of_freedom = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                # 磁石が隣接するかチェック
                magnet_nearby = any(0 <= i + di < H and 0 <= j + dj < W and grid[i + di][j + dj] == '#' for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)])
                if not magnet_nearby:
                    print(f"Starting BFS from ({i}, {j})")  # Debug print
                    max_degree_of_freedom = max(max_degree_of_freedom, bfs(grid, i, j, H, W))

    print(max_degree_of_freedom)

if __name__ == "__main__":
    main()
