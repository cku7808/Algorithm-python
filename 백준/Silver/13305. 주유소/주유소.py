N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
dp = [0] * N
dp[0] = dist[0] * price[0]
max_dp = 0
for i in range(1, N-1):
    dp[i] = min(dp[i-1] + (price[i-1] * dist[i]), dp[i-1] + (price[i] * dist[i]))
    if dp[i] > max_dp:
        max_dp = dp[i]
print(max_dp)