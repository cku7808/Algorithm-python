N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = 0
tmp = price[0]
tmp_len = dist[0]

for idx in range(1, N-1):
    if tmp < price[idx]:
         tmp_len += dist[idx]
    else:
        cost += tmp * tmp_len
        tmp = price[idx]
        tmp_len = dist[idx]
else:
    cost += tmp*tmp_len

print(cost)
