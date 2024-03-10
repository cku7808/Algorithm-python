import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0]*(n+1)
    if n <= 2:
        print(n)
    else:
        dp[1],dp[2], dp[3] = 1, 2, 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])
