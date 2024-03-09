import sys

n, k = map(int, sys.stdin.readline().split())
inf = float("inf")
dp = [inf]*(k+1)
dp[0] = 0

coins = list(set([int(sys.stdin.readline()) for _ in range(n)]))

for i in range(1, k+1):
    for coin in coins:
        if coin > i:
            continue
        if dp[i-coin] != inf:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] != inf:
    print(dp[k])
else:
    print(-1)
