import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(i,j):
    dxs = [0,0,1,-1]
    dys = [1,-1,0,0]
    q = deque([(i,j)])
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y
            if 0<=nx<=n-1 and 0<=ny<=m-1:
                if grid[nx][ny] == 0:
                    dist[nx][ny] = 0
                elif not visited[nx][ny] and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True

flag = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            dist[i][j] = 0
            bfs(i,j)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            dist[i][j] = 0
            
for elem in dist:
    print(*elem)
