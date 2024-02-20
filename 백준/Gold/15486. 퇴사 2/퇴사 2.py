import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)

for i in range(n):
    t,p = map(int, sys.stdin.readline().split())

    dp[i+1] = max(dp[i+1], dp[i]) # 이전값과 비교
    if i+t < n+1:
        dp[i+t] = max(dp[i+t], dp[i]+p)
print(dp[-1])
