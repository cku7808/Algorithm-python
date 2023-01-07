import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
grid = []

for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i,j))

dxs = [1,-1,0,0]
dys = [0,0,1,-1]

while q:
    x,y = q.popleft()
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
            q.append((nx,ny))
            grid[nx][ny] = grid[x][y] + 1

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans,max(grid[i]))
print(ans-1)


