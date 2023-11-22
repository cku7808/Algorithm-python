import sys
from collections import deque
import copy

n,m = map(int, sys.stdin.readline().split())

grid = []

for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

# 바이러스 퍼뜨리기 & 안전지대 수 세기
def spread_count():
    global ans
    q = deque()
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    visited = [[False]*m for _ in range(n)]
    test_grid = copy.deepcopy(grid)
    
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y
            if -1<nx<n and -1<ny<m and not visited[nx][ny]:
                if test_grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    test_grid[nx][ny] = 2
                    q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)
                

# 벽 세우기
def make_wall(cnt):
    global ans
    if cnt == 3:
        spread_count()
        return 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                make_wall(cnt+1)
                grid[i][j] = 0


ans = 0
make_wall(0)
print(ans)
