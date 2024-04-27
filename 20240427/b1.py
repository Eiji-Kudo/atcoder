def find_mismatched_cell():
    N = int(input())
    grid_A = [input() for _ in range(N)]
    grid_B = [input() for _ in range(N)]
    
    # 異なるセルを探す
    for i in range(N):
        for j in range(N):
            if grid_A[i][j] != grid_B[i][j]:
                # 1-indexedで出力するため、i+1, j+1を出力
                print(i + 1, j + 1)
                return

if __name__ == "__main__":
    find_mismatched_cell()