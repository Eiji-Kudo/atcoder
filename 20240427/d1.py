import sys
from collections import deque

def bfs(grid, start_row, start_col, H, W):
    # Initialize the queue with the start position and mark it as visited
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])  # Use a set of tuples for visited
    count = 1  # Start count at 1 since the start position is also counted
    # Define possible directions to move in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()  # Get the current position from the queue
        for dr, dc in directions:  # Check all possible directions
            nr, nc = r + dr, c + dc  # Compute the new position
            # Check if the new position is within bounds and not visited
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.' and (nr, nc) not in visited:
                visited.add((nr, nc))  # Mark the new position as visited
                queue.append((nr, nc))  # Add the new position to the queue
                count += 1  # Increase the count of accessible cells
    return count  # Return the total number of accessible cells

def main():
    # Read the height and width of the grid
    H, W = map(int, input().strip().split())
    # Read the grid
    grid = [input().strip() for _ in range(H)]

    max_degree_of_freedom = 0  # Initialize the maximum degree of freedom to 0
    # Iterate over each cell in the grid
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':  # Only start BFS if the cell is empty (not blocked)
                degree = bfs(grid, i, j, H, W)  # Perform BFS from this cell
                max_degree_of_freedom = max(max_degree_of_freedom, degree)  # Update the maximum if needed

    print(max_degree_of_freedom if max_degree_of_freedom > 0 else 1)  # Output the result

if __name__ == "__main__":
    main()
