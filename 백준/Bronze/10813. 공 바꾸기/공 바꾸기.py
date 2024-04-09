import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(range(n+1))
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    arr[a], arr[b] = arr[b], arr[a]
print(*arr[1:])