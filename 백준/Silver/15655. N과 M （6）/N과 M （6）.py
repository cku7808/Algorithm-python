import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
result = []

def backtrack(idx):
    if len(result) == m:
        print(*result)
        return

    for i in range(idx,n):
        result.append(arr[i])
        backtrack(i+1)
        result.pop()
backtrack(0)
