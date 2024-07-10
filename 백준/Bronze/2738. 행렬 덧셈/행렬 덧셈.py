import sys

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        ans[i][j] = a[i][j] + b[i][j]

    print(*ans[i])
