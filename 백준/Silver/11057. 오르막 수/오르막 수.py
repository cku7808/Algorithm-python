import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(n+1)]
dp[0] = [1]*10


for i in range(1, n+1):
    dp[i][0] = 1
    for j in range(1,10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][9]%10007)
