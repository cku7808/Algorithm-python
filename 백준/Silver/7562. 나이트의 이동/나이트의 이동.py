import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    dest_x, dest_y = map(int, sys.stdin.readline().split())

    grid = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    dxs = [1,2,2,1,-1,-2,-2,-1]
    dys = [-2,-1,1,2,-2,-1,1,2]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx,ny = dx+x, dy+y

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                q.append((nx,ny))
                visited[nx][ny] = True
                grid[nx][ny] = grid[x][y] + 1
    print(grid[dest_x][dest_y])
