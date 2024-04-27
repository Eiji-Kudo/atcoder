import sys

def can_form_airport_code(S, T):
    n = len(S)
    # 文字の出現位置を追跡する
    positions = {chr(i): [] for i in range(ord('a'), ord('z') + 1)}
    for index, char in enumerate(S):
        positions[char].append(index)
    
    # 3文字のTを確認する
    def check_three_chars():
        # Tの各文字に対してS中の位置を探す
        indices = [-1, -1, -1]
        for i, char in enumerate(T):
            lower_char = char.lower()
            pos_list = positions[lower_char]
            # 前の文字より後ろにある位置を見つける
            last_index = indices[i-1] if i > 0 else -1
            found = False
            for pos in pos_list:
                if pos > last_index:
                    indices[i] = pos
                    found = True
                    break
            if not found:
                return False
        return True
    
    # 2文字のTを確認する（末尾はX）
    def check_two_chars_and_x():
        if T[2] != 'X':
            return False
        indices = [-1, -1]
        for i, char in enumerate(T[:2]):
            lower_char = char.lower()
            pos_list = positions[lower_char]
            last_index = indices[i-1] if i > 0 else -1
            found = False
            for pos in pos_list:
                if pos > last_index:
                    indices[i] = pos
                    found = True
                    break
            if not found:
                return False
        return True

    return "Yes" if check_three_chars() or check_two_chars_and_x() else "No"

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    S = data[0]
    T = data[1]
    print(can_form_airport_code(S, T))
