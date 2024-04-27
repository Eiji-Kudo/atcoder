def minimum_swaps_to_sort(n, a):
    # a[i]がi+1になるまでのスワップを記録
    # 場所を記録する辞書
    index_by_value = {value: i for i, value in enumerate(a)}
    swaps = []
    
    for i in range(n):
        correct_value = i + 1
        if a[i] != correct_value:
            # 正しい位置にない要素を見つける
            swap_with_idx = index_by_value[correct_value]
            # スワップ
            a[i], a[swap_with_idx] = a[swap_with_idx], a[i]
            # 辞書も更新
            index_by_value[a[swap_with_idx]] = swap_with_idx
            index_by_value[a[i]] = i
            # スワップ操作を記録
            swaps.append((i + 1, swap_with_idx + 1))
    
    # 結果を出力
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

n = int(input())
a = list(map(int, input().split()))
minimum_swaps_to_sort(n, a)
