import sys
sys.setrecursionlimit(10**5)

n,m = map(int, sys.stdin.readline().split())
grid = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    grid[u].append(v)
    grid[v].append(u)

def dfs(grid, v, visited):
    global cnt
    visited[v] = True
    for elem in grid[v]:
        if not visited[elem]:
            dfs(grid,elem, visited)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(grid, i, visited)
        cnt += 1

print(cnt)
