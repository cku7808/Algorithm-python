import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

result = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for v in range(m):
            result[i][j] += a[i][v] * b[v][j]

for elem in result:
    print(*elem)
