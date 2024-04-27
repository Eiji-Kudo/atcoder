def count_balls(N, A):
    stack = []
    
    for a in A:
        # ボールのサイズは 2^a
        size = 2 ** a
        
        # スタックにボールを追加し、条件に合う限り処理を続ける
        while True:
            if stack and stack[-1] == size:
                # トップのボールが同じサイズなら合体させる
                stack.pop()
                size *= 2
            else:
                # 合体できない場合は現在のサイズのボールをスタックに追加
                stack.append(size)
                break
    
    # スタックに残っているボールの数が答え
    return len(stack)


N = int(input())
A = list(map(int, input().split()))


print(count_balls(N, A))
