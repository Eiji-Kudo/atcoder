def check_contest_abbreviation(s):
    # Sから数字部分だけを取り出す
    number_part = int(s[3:])  # "ABC"の後の数字部分を整数型に変換
    
    # 範囲内かつ316ではないことをチェック
    if 1 <= number_part <= 349 and number_part != 316:
        return "Yes"
    else:
        return "No"

# 標準入力から文字列Sを読み込む
s = input().strip()

# 結果を出力
print(check_contest_abbreviation(s))
