import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

grid = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    tmp = []
    for elem in s:
        tmp.append(int(elem))
    grid.append(tmp)

visited = [[False]*m for _ in range(n)]


q = deque([(0,0)])
visited[0][0] = True

dxs = [1,-1,0,0]
dys = [0,0,1,-1]

while q:
    x,y = q.popleft()

    for dx, dy in zip(dxs,dys):
        nx, ny = dx+x, dy+y

        if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1 and visited[nx][ny] == False:
            q.append((nx,ny))
            visited[nx][ny] = True
            grid[nx][ny] = grid[x][y] + 1

print(grid[n-1][m-1])
