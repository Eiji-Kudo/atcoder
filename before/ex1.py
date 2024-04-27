from math import gcd
from functools import reduce
from collections import defaultdict

MOD = 998244353

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

def all_divisors(n):
    factors = prime_factors(n)
    divisors = [1]
    for p, exp in factors.items():
        current = []
        for d in divisors:
            for e in range(1, exp + 1):
                current.append(d * (p ** e))
        divisors += current
    return sorted(divisors)
def solve(N, M, A):
    # M の素因数分解
    factors = prime_factors(M)
    # 全ての約数を求める
    divisors = all_divisors(M)
    # 各約数についてのカウンタ
    dp = [0] * (max(divisors) + 1)
    # 1は空の部分列に対応
    dp[1] = 1

    # A の各要素に対して
    for num in A:
        # num が割り切れる約数について処理
        for d in sorted(divisors, reverse=True):
            if num % d == 0:
                dp[d] = (dp[d] + dp[d // gcd(d, num)]) % MOD

    return dp[M]

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))
