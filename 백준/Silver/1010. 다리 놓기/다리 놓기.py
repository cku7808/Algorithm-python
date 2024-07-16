import sys

#mCn*n!
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    
    dp = [1]*(m+1)
    for i in range(1, m+1):
        dp[i] = dp[i-1]*i

    print(dp[m]//(dp[n]*dp[m-n]))
