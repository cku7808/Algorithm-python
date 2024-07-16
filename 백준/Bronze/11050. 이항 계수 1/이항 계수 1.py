import sys

n, k = map(int, sys.stdin.readline().split())
tmp = 1
dp = [1]
for i in range(1,11):
    tmp *= i
    dp.append(tmp)

print(dp[n]//(dp[n-k]*dp[k]))
