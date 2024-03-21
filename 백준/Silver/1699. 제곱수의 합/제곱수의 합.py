import sys, math

n = int(sys.stdin.readline())

dp = [float("inf")]*(n+1)

for i in range(1, int(math.sqrt(n))+1):
    num = i*i
    for j in range(1, n+1):
        if j%num == 0:
            dp[j] = min(dp[j], j//num)
        else:
            dp[j] = min(dp[j], j//num+dp[j%num])
print(dp[n])
