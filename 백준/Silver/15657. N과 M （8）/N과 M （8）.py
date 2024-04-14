import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = []

def backtrack(idx):
    if len(result) == m:
        print(*result)
        return

    for i in range(idx, n):
        result.append(arr[i])
        backtrack(i)
        result.pop()

backtrack(0)
