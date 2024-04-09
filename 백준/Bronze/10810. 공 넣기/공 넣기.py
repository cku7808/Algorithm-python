import sys

n,m = map(int, sys.stdin.readline().split())
arr = [0]*(n+1)

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    arr[i:j+1] = [k]*(j+1-i)
print(*arr[1:])