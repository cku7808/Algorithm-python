import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs(a,b,c):
    q = deque([(a,b,c)])

    dxs = [0,0,-1,1]
    dys = [-1,1,0,0]

    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        
        for dx, dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y

            if -1<nx<n and -1<ny<m:
                if grid[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx,ny,z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                if grid[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))

    return -1

print(bfs(0,0,0))

