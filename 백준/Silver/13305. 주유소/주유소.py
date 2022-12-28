import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

ans = 0
min_cost = price[0]
for i in range(n-1):
    if price[i]< min_cost:
        min_cost = price[i]
    ans += min_cost*length[i]

print(ans)
