def process_balls(N, A):
    # 数値をそのまま使うため、2のべき乗変換は不要
    stack = []
    
    for a in A:
        current = a  # 現在のボールのサイズ
        
        # スタックが空でなく、かつスタックの最後の要素と同じならばマージを行う
        while stack and stack[-1] == current:
            stack.pop()      # 前の要素を取り出し
            current += 1     # マージにより要素サイズを+1する
        
        # 更新された現在の要素をスタックに追加
        stack.append(current)
    
    # 最終的にスタックに残っている要素の数を返す
    return len(stack)

# 入力
N = int(input())
A = list(map(int, input().split()))

# 結果出力
print(process_balls(N, A))
