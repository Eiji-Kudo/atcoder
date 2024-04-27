def count_teeth_after_treatments(N, Q, treatments):
    teeth = [True] * N
    for t in treatments:
        index = t - 1
        teeth[index] = not teeth[index]
    return sum(teeth)


N, Q = map(int, input().split())
treatments = list(map(int, input().split()))

print(count_teeth_after_treatments(N, Q, treatments))