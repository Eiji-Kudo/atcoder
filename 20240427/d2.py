import sys

def find_free_cells(grid, H, W):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上, 下, 左, 右
    free_cells = set()

    for r in range(H):
        for c in range(W):
            if grid[r][c] == '.':
                print(f"  Checking cell ({r}, {c})")  # Debug print
                # 磁石が隣接しているか調べる
                is_magnet_adjacent = False
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '#':
                        is_magnet_adjacent = True
                        print(f"    Magnet found at ({nr}, {nc})")  # Debug print
                        break

                if not is_magnet_adjacent:
                    free_cells.add((r, c))
                    print(f"  Cell ({r}, {c}) is free")  # Debug print

    print(f"Total free cells: {len(free_cells)}")  # Debug print
    return free_cells

def main():
    H, W = map(int, sys.stdin.readline().strip().split())
    grid = [sys.stdin.readline().strip() for _ in range(H)]
    print(f"Grid size: {H}x{W}")  # Debug print
    print("Grid:")  # Debug print
    for row in grid:
        print(f"  {row}")  # Debug print

    free_cells = find_free_cells(grid, H, W)
    print(f"Number of free cells: {len(free_cells)}")  # Debug print

if __name__ == "__main__":
    main()
