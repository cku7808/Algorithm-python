import sys

def backtrack(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            backtrack(cnt+1)
            arr.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []
backtrack(0)